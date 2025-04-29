from network import FaceXFormer
from transformers import Trainer, TrainingArguments
import torch
import datasets
import os
from datetime import datetime

device = "cuda:0"
weight_path = "ckpts/model.pt"
dtype = torch.half
model = FaceXFormer().to(device)
checkpoint = torch.load(weight_path, map_location=device)
model.load_state_dict(checkpoint["state_dict_backbone"])
model = model.to(dtype=dtype)

dataset = datasets.load_dataset("json", data_files="data/all.json", split="train")
dataset = dataset.cast_column("img", datasets.Image())
dataset = dataset.train_test_split(0.2, shuffle=True, seed=42)

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
        learning_rate=1e-4,
        save_strategy="steps",
        save_steps=100,
        save_total_limit=3,
        save_safetensors=False,
        # report_to=["tensorboard"],
    ),
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    # data_collator=lambda: None,
)

trainer.train()
