import cv2

cap = cv2.VideoCapture("ex1.mp4")
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"해상도: {width} x {height}")
cap.release()