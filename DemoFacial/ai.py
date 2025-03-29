import torch
import torchvision
from torchvision.transforms import InterpolationMode
from facexformer.network import FaceXFormer
from facenet_pytorch import MTCNN
from dataclasses import dataclass
from PIL import Image

device = "cuda:0"
dtype = torch.float32
weights_path = "ckpts/model.pt"
face_model_path = "ckpts/blaze_face_short_range.tflite"

mtcnn = MTCNN(keep_all=True, device=device).eval()
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


def load_model(weights_path):
    model = FaceXFormer().to(device)
    checkpoint = torch.load(weights_path, map_location=device)
    model.load_state_dict(checkpoint["state_dict_backbone"])
    model = model.eval()
    model = model.to(dtype=dtype)
    # model = torch.compile(model, mode="reduce-overhead")
    return model


model = load_model(weights_path)


def adjust_bbox(
    x_min, y_min, x_max, y_max, image_width, image_height, margin_percentage=50
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


def denorm_points(points, h, w, align_corners=False):
    if align_corners:
        denorm_points = (
            (points + 1) / 2 * torch.tensor([w - 1, h - 1]).to(points).view(1, 1, 2)
        )
    else:
        denorm_points = (
            (points + 1) * torch.tensor([w, h]).to(points).view(1, 1, 2) - 1
        ) / 2

    return denorm_points


@dataclass
class FaceImg:
    image: Image
    x_min: int
    y_min: int


def get_faces_img(img: Image):
    with torch.inference_mode():
        boxes, probs = mtcnn.detect(img)
    if boxes is None or len(boxes) == 0:
        return []
    results: list[FaceImg] = []
    for box in boxes:
        x_min, y_min, x_max, y_max = box[0], box[1], box[2], box[3]

        # Padding
        x_min, y_min, x_max, y_max = adjust_bbox(
            x_min, y_min, x_max, y_max, img.width, img.height
        )
        image = img.crop((int(x_min), int(y_min), int(x_max), int(y_max)))
        results.append(FaceImg(image, int(x_min), int(y_min)))

    return results


@dataclass
class Face:
    image: torch.Tensor
    x_min: int
    y_min: int
    original_w: int
    original_h: int


def get_faces(img: Image):
    images = get_faces_img(img)
    images = [
        Face(
            transforms_image(face_image.image),
            face_image.x_min,
            face_image.y_min,
            face_image.image.size[0],
            face_image.image.size[1],
        )
        for face_image in images
    ]
    return images


def get_landmarks(faces: list[Face]):
    if len(faces) == 0:
        return []

    images = torch.stack([face.image for face in faces]).to(device=device, dtype=dtype)

    tasks = torch.tensor([1] * len(faces), device=device, dtype=dtype)
    with torch.inference_mode():
        # with torch.amp.autocast("cuda"):
        (
            batch_landmarks,
            headposes,
            attributes,
            visibilities,
            ages,
            geders,
            races,
            segs,
        ) = model(images, None, tasks)
    batch_denormed = [
        denorm_points(landmarks, face.original_h, face.original_w)[0]
        for landmarks, face in zip(batch_landmarks.view(-1, 68, 2), faces)
    ]

    results = []
    for landmarks, face in zip(batch_denormed, faces):
        results.append([(x + face.x_min, y + face.y_min) for x, y in landmarks])

    return results
