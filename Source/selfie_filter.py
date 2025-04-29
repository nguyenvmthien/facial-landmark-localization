import os
import numpy as np
import cv2
import landmark_detection
import gradio as gr
from mtcnn_facedetection import detect_faces


def apply_sunglasses(image, landmarks, sunglasses_img):
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
        angle = -np.degrees(
            np.arctan2(
                right_eye_center[1] - left_eye_center[1],
                right_eye_center[0] - left_eye_center[0],
            )
        )

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
            borderValue=(0, 0, 0, 0),
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
                    roi[:, :, c] = (
                        glasses_roi[:, :, c] * alpha + roi[:, :, c] * (1 - alpha)
                    ).astype(np.uint8)
                result[y1:y2, x1:x2] = roi

    return result


def do_facial_landmark_recognition(
    image: np.ndarray, face_boxes: list[landmark_detection.BoundingBox]
):
    faces = landmark_detection.get_faces(image, face_boxes)
    landmarks_batch = landmark_detection.get_landmarks(faces)
    return landmarks_batch


def do_facial_landmark_recognition_with_mtcnn(image: np.ndarray, sunglasses_img):
    face_boxes = detect_faces(image)
    landmarks_batch = do_facial_landmark_recognition(image, face_boxes)
    return apply_sunglasses(image, landmarks_batch, sunglasses_img)


def process_video(input_path, sunglasses_img):
    output_path = os.path.join(
        os.path.dirname(input_path), "output_" + os.path.basename(input_path)
    )
    # Open the input video
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        gr.Error(f"Error opening input video file: {input_path}")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_count = 0

    # Process each frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame
        processed_frame = do_facial_landmark_recognition_with_mtcnn(
            frame, sunglasses_img
        )

        # Write the frame
        out.write(processed_frame)

    # Release resources
    cap.release()
    out.release()
    gr.Info(f"Video processing complete. Output saved to: {output_path}")
    return output_path
