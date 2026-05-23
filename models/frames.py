import cv2
import numpy as np
from models.space_detection import check_space,pos_list,slot_history
capture = cv2.VideoCapture("parking_1920_1080_loop.mp4")



for i in range(len(pos_list)):
    slot_history[i] = []

def generate_frames():
    while True:

        if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
            capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

        success, img = capture.read()

        if not success:
            break

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        blur_img = cv2.GaussianBlur(gray_img, (5, 5), 1)

        image_threshold = cv2.adaptiveThreshold(
            blur_img,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            25,
            16
        )

        image_median = cv2.medianBlur(image_threshold, 5)

        kernel = np.ones((3, 3), np.uint8)

        image_dilate = cv2.dilate(
            image_median,
            kernel,
            iterations=1
        )

        check_space(image_dilate, img)

        _, buffer = cv2.imencode('.jpg', img)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )
