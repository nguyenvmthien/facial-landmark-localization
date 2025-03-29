# import streamlit as st
# from streamlit_webrtc import webrtc_streamer
# import torch
# torch.classes.__path__ = []

import gradio as gr
from fastrtc import WebRTC
from fastrtc import VideoStreamHandler
import av
from PIL import Image, ImageDraw
import ai
import numpy as np
from time import time


radius = 2


def do_facial_landmark_recognition(image: Image):
    faces = ai.get_faces(image)
    landmarks_batch = ai.get_landmarks(faces)
    drawer = ImageDraw.Draw(image)
    drawer.text((0, 0), "This worked", fill="red")

    for i, landmarks in enumerate(landmarks_batch):
        for landmark in landmarks:
            drawer.circle(landmark, radius, fill="red")

    return image


def video_frame_callback_gradio(frame: np.array):
    img = Image.fromarray(frame)
    flipped = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    flipped = do_facial_landmark_recognition(flipped)

    return np.array(flipped)


def video_frame_callback_streamlit(frame: av.VideoFrame):
    img = frame.to_image()
    flipped = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

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
                video_frame_callback_gradio, fps=10, skip_frames=True
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
    if '--test' in sys.argv:
        test()
    else:
        demo.launch()
