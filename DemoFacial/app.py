# import streamlit as st
# from streamlit_webrtc import webrtc_streamer
# import torch
# torch.classes.__path__ = []

import gradio as gr
from fastrtc import WebRTC
from fastrtc import VideoStreamHandler
import av
from PIL import Image, ImageDraw
import landmark_detection
import numpy as np
from time import time
import cv2
from mtcnn_facedetection import detect_faces


radius = 2


def do_facial_landmark_recognition(
    image: np.ndarray, face_boxes: list[landmark_detection.BoundingBox]
):
    faces = landmark_detection.get_faces(image, face_boxes)
    landmarks_batch = landmark_detection.get_landmarks(faces)

    for i, landmarks in enumerate(landmarks_batch):
        for landmark in landmarks:
            image = cv2.circle(image, landmark, radius, (255, 0, 0), -1)

    return image

def do_facial_landmark_recognition_with_mtcnn(image: np.ndarray):
    face_boxes = detect_faces(image)
    return do_facial_landmark_recognition(image, face_boxes)

def video_frame_callback_gradio(frame: np.array):
    flipped = cv2.flip(frame, 1)

    flipped = do_facial_landmark_recognition_with_mtcnn(flipped)

    return flipped


def video_frame_callback_streamlit(frame: av.VideoFrame):
    img = frame.to_ndarray()
    flipped = cv2.flip(img, 1)

    flipped = do_facial_landmark_recognition(flipped)

    return flipped


# st.header("This is a test")
# webrtc_streamer(key="sample", video_frame_callback=video_frame_callback_streamlit)

# do_facial_landmark_recognition(Image.open("tmp.jpg")).save("gg.png")

css = """.my-group {max-width: 600px !important; max-height: 600px !important;}
         .my-column {display: flex !important; justify-content: center !important; align-items: center !important;}"""

with gr.Blocks(css=css) as demo:
    gr.HTML(
        """
        <h1 style='text-align: center'>
        YOLOv10 Webcam Stream (Powered by WebRTC ⚡️)
        </h1>
        """
    )
    with gr.Column(elem_classes=["my-column"]):
        with gr.Group(elem_classes=["my-group"]):
            image = WebRTC(label="Stream", rtc_configuration=None)
        image.stream(
            fn=VideoStreamHandler(
                video_frame_callback_gradio, fps=12, skip_frames=True
            ),
            inputs=[image],
            outputs=[image],
            time_limit=None,
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


import sys

if __name__ == "__main__":
    if "--test" in sys.argv:
        test()
    else:
        demo.launch()
