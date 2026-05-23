"""
script ini untuk mengambil frame
pertama pada video yang akan diberi anotasi
script ini harus dijalankan sekali saja.
"""



import cv2

# Load video
capture = cv2.VideoCapture("parking_1920_1080_loop.mp4")

# Read first frame
success, frame = capture.read()

if success:

    # Save first frame as image
    cv2.imwrite("first_frame.jpg", frame)

    print("First frame saved as first_frame.jpg")

else:
    print("Failed to read video")

capture.release()

