import os
import torch
import torchvision
import datasets
import PIL.Image
import PIL.ImageDraw
from datetime import datetime
from dataclasses import dataclass
from network import FaceXFormer
from transformers import Trainer, TrainingArguments
from torchvision.transforms import InterpolationMode

device = "cuda:0"
dtype = torch.float32


def load_model(weight_path):
    model = FaceXFormer().to(device)
    # checkpoint = torch.load(weight_path, map_location=device)
    # model.load_state_dict(checkpoint["state_dict_backbone"])
    model = model.to(dtype=dtype)
    return model


def load_dataset(dataset_path):
    dataset = datasets.load_dataset("json", data_files=dataset_path, split="train")
    # dataset = dataset.cast_column("img", datasets.Image())
    dataset = dataset.train_test_split(0.2, shuffle=True, seed=42)
    return dataset


@dataclass
class DataCollator:
    image_base_path: str
    return_tensors: str = "pt"

    transforms_image = torchvision.transforms.Compose(
        [
            torchvision.transforms.Resize(
                size=(224, 224), interpolation=InterpolationMode.BICUBIC
            ),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(
                mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
            ),
        ]
    )

    def __call__(self, features: list[dict], return_tensors=None):
        batch = {
            "labels": [],
            "x": [],
            # "tasks": torch.ones(len(features)),
        }

        for feature in features:
            image = PIL.Image.open(
                os.path.join(self.image_base_path, feature["img"])
            ).convert("RGB")
            label = feature["pts"]
            image, x_min, y_min, width = self.cut_face(image, label)
            batch["labels"].append([[x - x_min, y - y_min] for x, y in label])
            batch["x"].append(self.transforms_image(image))

        # print("This was called")
        batch["labels"] = torch.Tensor(batch["labels"]) / width * 2 - 1
        batch["x"] = torch.stack(batch["x"])
        return batch

    def adjust_bbox(
        self,
        x_min: int,
        y_min: int,
        x_max: int,
        y_max: int,
        image_width: int,
        image_height: int,
        margin_percentage=50,
    ):
        width = x_max - x_min
        height = y_max - y_min

        increase_width = width * (margin_percentage / 100.0) / 2
        increase_height = height * (margin_percentage / 100.0) / 2

        x_min_adjusted = max(0, x_min - increase_width)
        y_min_adjusted = max(0, y_min - increase_height)
        x_max_adjusted = min(image_width, x_max + increase_width)
        y_max_adjusted = min(image_height, y_max + increase_height)

        return x_min_adjusted, y_min_adjusted, x_max_adjusted, y_max_adjusted

    def cut_face(self, img: PIL.Image.Image, pts: list[list[float]]):
        x_vals = [point[0] for point in pts]
        y_vals = [point[1] for point in pts]
        x_min, x_max = int(min(x_vals)), int(max(x_vals))
        y_min, y_max = int(min(y_vals)), int(max(y_vals))
        # Make the image square
        face_img_w, face_img_h = x_max - x_min, y_max - y_min
        side_len = max(face_img_w, face_img_h)
        x_min = max(0, x_min - (side_len - face_img_w) / 2)
        x_max = min(img.width, x_max + (side_len - face_img_w) / 2)
        y_min = max(0, y_min - (side_len - face_img_h) / 2)
        y_max = min(img.height, y_max + (side_len - face_img_h) / 2)

        # Padding
        x_min, y_min, x_max, y_max = self.adjust_bbox(
            x_min, y_min, x_max, y_max, img.width, img.height
        )
        image = img.crop((int(x_min), int(y_min), int(x_max), int(y_max)))
        # image: torch.Tensor = self.transforms_image(image)
        return image, x_min, y_min, image.width


def main():
    dataset = load_dataset(dataset_path="data/all.json")
    # print(dataset["train"][78])
    # exit(1)
    model = load_model(weight_path="ckpts/model.pt")
    trainer = Trainer(
        model,
        args=TrainingArguments(
            output_dir=os.path.join(
                "saves", datetime.strftime(datetime.now(), "%Y%m%d-%H%M")
            ),
            eval_strategy="steps",
            eval_steps=100,
            optim="adamw_torch",
            per_device_train_batch_size=1,
            per_device_eval_batch_size=1,
            gradient_accumulation_steps=1,
            learning_rate=1e-4,
            save_strategy="steps",
            save_steps=100,
            save_total_limit=3,
            save_safetensors=False,
            remove_unused_columns=False,
            report_to=["tensorboard"],
            max_steps=200,
            logging_steps=1,
        ),
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        data_collator=DataCollator(image_base_path="data"),
    )

    trainer.train()


def test():
    dataset = load_dataset(dataset_path="data/all.json")
    data_collator = DataCollator(image_base_path="data")
    features = dataset["train"].select(range(10))

    for i, feature in enumerate(features):
        image = PIL.Image.open(
            os.path.join(data_collator.image_base_path, feature["img"])
        ).convert("RGB")
        label = feature["pts"]
        image, x_min, y_min, width = data_collator.cut_face(image, label)
        label = [
            [(x - x_min) / width * 2 - 1, (y - y_min) / width * 2 - 1] for x, y in label
        ]
        image_draw = PIL.ImageDraw.ImageDraw(image)
        print(image.size)
        print(label[0])
        for x, y in label:
            x = (x + 1) * width / 2
            y = (y + 1) * width / 2
            image_draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill="blue")

        image.save(f"out-{i}.png")

    # print("This was called")


if __name__ == "__main__":
    main()
    # test()
