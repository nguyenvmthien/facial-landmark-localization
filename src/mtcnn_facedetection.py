from landmark_detection import device, BoundingBox
from facenet_pytorch import MTCNN
import numpy as np

mtcnn = MTCNN(keep_all=True, device=device).eval()


def detect_faces(img) -> list[BoundingBox]:
    boxes, probs = mtcnn.detect(img)
    return [
        BoundingBox(
            x_min=int(box[0]),
            y_min=int(box[1]),
            x_max=int(box[2]),
            y_max=int(box[3]),
        )
        for box in boxes
    ] if boxes is not None else []
