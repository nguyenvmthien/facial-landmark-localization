# import streamlit as st
# from streamlit_webrtc import webrtc_streamer
# import torch
# torch.classes.__path__ = []

import sys
import os
from glob import glob
import gradio as gr
from fastrtc import WebRTC
from fastrtc import VideoStreamHandler
from PIL import Image
import landmark_detection
import numpy as np
from time import time
import cv2
from mtcnn_facedetection import detect_faces
from selfie_filter import apply_sunglasses, process_video


radius = 2
filter_img = None


def do_facial_landmark_recognition(
    image: np.ndarray, face_boxes: list[landmark_detection.BoundingBox]
):
    faces = landmark_detection.get_faces(image, face_boxes)
    landmarks_batch = landmark_detection.get_landmarks(faces)

    for i, landmarks in enumerate(landmarks_batch):
        for landmark in landmarks:
            image = cv2.circle(image, landmark, radius, (255, 0, 0), -1)

    return image, landmarks_batch


def do_facial_landmark_recognition_with_mtcnn(image: np.ndarray):
    face_boxes = detect_faces(image)
    return do_facial_landmark_recognition(image, face_boxes)


def video_frame_callback_gradio(frame: np.array):
    flipped = cv2.flip(frame, 1)

    flipped, landmarks_batch = do_facial_landmark_recognition_with_mtcnn(flipped)
    # Apply sunglasses filter
    image = apply_sunglasses(flipped, landmarks_batch, filter_img)

    return image  # , AdditionalOutputs(flipped, flipped)


css = """.my-group {max-width: 600px !important;}
         .my-column {display: flex !important; justify-content: center !important; align-items: center !important;}"""

image_extensions = [
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.gif",
    "*.bmp",
    "*.tiff",
    "*.webp",
]
all_image_files = []

for ext in image_extensions:
    pattern = os.path.join("images", "**", ext)  # '**' for recursive search
    image_files = glob(pattern, recursive=True)
    all_image_files.extend(image_files)
all_image_files.sort()


with gr.Blocks(css=css) as demo:
    with gr.Column(elem_classes=["my-column"]):
        gr.HTML(
            """
            <h1 style='text-align: center'>
            Live Filter with FaceXFormer
            </h1>
            """
        )
        with gr.Group(elem_classes=["my-group"]):
            selected_filter = gr.Dropdown(
                choices=all_image_files,
                label="Choose filter",
                value="images/sunglasses_1.png",
            )

            def change_filter(filter_path):
                global filter_img
                try:
                    filter_img = cv2.imread(filter_path, cv2.IMREAD_UNCHANGED)
                except:
                    gr.Error("Error open" + filter_path)

            change_filter(selected_filter.value)

            selected_filter.change(
                change_filter, inputs=[selected_filter], show_progress="full"
            )

        with gr.Group(elem_classes=["my-group"]):
            stream = WebRTC(label="Stream", rtc_configuration=None)
            stream.stream(
                fn=VideoStreamHandler(
                    video_frame_callback_gradio, fps=12, skip_frames=True
                ),
                inputs=[stream],
                outputs=[stream],
                time_limit=None,
            )

        with gr.Group(elem_classes=["my-group"]):
            with gr.Column(elem_classes=["my-column"]):
                gr.HTML(
                    """
                    <h1 style='text-align: center'>
                    Or just apply the filter to a video
                    </h1>
                    """
                )
                input_video = gr.Video(sources="upload", include_audio=False)
                output_video = gr.Video(interactive=False, include_audio=False)
                submit = gr.Button(variant="primary")
            with gr.Column(elem_classes=["my-column"]):
                submit.click(
                    lambda input_path: process_video(input_path, filter_img),
                    inputs=[input_video],
                    outputs=[output_video],
                    show_progress="full",
                )


def test(times=10):
    image = Image.open("tmp.jpg").resize((512, 512))
    # faces = ai.get_faces(image)
    start = time()
    frame_times = [None] * times
    for i in range(times):
        before = time()
        do_facial_landmark_recognition(image)
        after = time()
        frame_times[i] = after - before
    end = time()

    print(f"Num Images: {times}")
    print(f"Total time: {end - start}")
    print(
        f"Max frametime: {max(frame_times)}, FPS: {1 / max(frame_times)}",
    )
    print(
        f"Min frametime: {min(frame_times)}, FPS: {1 / min(frame_times)}",
    )
    print(
        f"Avg frametime: {sum(frame_times) / len(frame_times)}, FPS: {1 / (sum(frame_times) / len(frame_times))}",
    )


if __name__ == "__main__":
    if "--test" in sys.argv:
        test()
    else:
        demo.launch()
