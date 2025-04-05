import sys
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
# Add this function to handle sunglasses overlay


def apply_sunglasses(image, landmarks):
    # Load sunglasses image (make sure this path exists)
    sunglasses_img = cv2.imread("images/sunglasses.png", cv2.IMREAD_UNCHANGED)

    # If image loading fails or no landmarks, return original image
    if sunglasses_img is None or not landmarks:
        return image

    # Create a copy of the image to overlay on
    result = image.copy()

    # Process each face
    for face_landmarks in landmarks:
        # We need at least the eye landmarks
        if len(face_landmarks) < 5:
            continue

        # Get eye landmarks
        left_eye_center = np.mean(face_landmarks[36:42], axis=0).astype(int)
        right_eye_center = np.mean(face_landmarks[42:48], axis=0).astype(int)

        # Calculate eye distance and angle
        eye_distance = np.linalg.norm(right_eye_center - left_eye_center)
        # Negate the angle to correct rotation direction
        angle = -np.degrees(np.arctan2(
            right_eye_center[1] - left_eye_center[1],
            right_eye_center[0] - left_eye_center[0]))

        # Size for sunglasses based on eye distance
        width = int(eye_distance * 2.5)
        height = int(width * sunglasses_img.shape[0] / sunglasses_img.shape[1])

        # Resize sunglasses
        sunglasses_resized = cv2.resize(sunglasses_img, (width, height))

        # Rotate the sunglasses image
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

        # Calculate new dimensions after rotation
        cos = np.abs(rotation_matrix[0, 0])
        sin = np.abs(rotation_matrix[0, 1])
        new_width = int((height * sin) + (width * cos))
        new_height = int((height * cos) + (width * sin))

        # Adjust rotation matrix
        rotation_matrix[0, 2] += (new_width / 2) - center[0]
        rotation_matrix[1, 2] += (new_height / 2) - center[1]

        # Perform the rotation
        rotated_glasses = cv2.warpAffine(
            sunglasses_resized,
            rotation_matrix,
            (new_width, new_height),
            flags=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=(0, 0, 0, 0)
        )

        # Position the sunglasses
        eye_center = ((left_eye_center + right_eye_center) // 2).astype(int)
        x = eye_center[0] - new_width // 2
        y = eye_center[1] - new_height // 2

        # Create ROI for overlay
        y1, y2 = max(0, y), min(result.shape[0], y + new_height)
        x1, x2 = max(0, x), min(result.shape[1], x + new_width)

        # ROI in the glasses image
        g_y1, g_y2 = max(0, -y), max(0, -y) + (y2 - y1)
        g_x1, g_x2 = max(0, -x), max(0, -x) + (x2 - x1)

        # Check if we have valid regions
        if g_y2 <= rotated_glasses.shape[0] and g_x2 <= rotated_glasses.shape[1]:
            roi = result[y1:y2, x1:x2]
            glasses_roi = rotated_glasses[g_y1:g_y2, g_x1:g_x2]

            # Apply alpha blending
            if glasses_roi.shape[2] == 4 and roi.shape[:2] == glasses_roi.shape[:2]:
                alpha = glasses_roi[:, :, 3] / 255.0
                for c in range(3):
                    roi[:, :, c] = (glasses_roi[:, :, c] * alpha +
                                    roi[:, :, c] * (1 - alpha)).astype(np.uint8)
                result[y1:y2, x1:x2] = roi

    return result

# Modify the facial landmark recognition function


def do_facial_landmark_recognition(
    image: np.ndarray, face_boxes: list[landmark_detection.BoundingBox]
):
    faces = landmark_detection.get_faces(image, face_boxes)
    landmarks_batch = landmark_detection.get_landmarks(faces)

    # Draw landmarks if desired (or comment this out to hide them)
    for i, landmarks in enumerate(landmarks_batch):
        for landmark in landmarks:
            image = cv2.circle(image, landmark, radius, (255, 0, 0), -1)

    # Apply sunglasses filter
    image = apply_sunglasses(image, landmarks_batch)

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


if __name__ == "__main__":
    if "--test" in sys.argv:
        test()
    else:
        demo.launch()
