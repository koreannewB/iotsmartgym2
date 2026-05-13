import time
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import state
from ultralytics import YOLO
import cv2
import base64
current_frame = None
model = YOLO('best.pt')

ZONES = {
    1: (0,   0, 600,  1920),
    2: (600, 0, 1080, 1920),
}

def is_person_in_zone(box, zone):
    x1, y1, x2, y2 = box
    zx1, zy1, zx2, zy2 = zone
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    return zx1 < cx < zx2 and zy1 < cy < zy2

def trail_detect_run():
    global current_frame
    print("런닝머신감지기능작동")
    cap = cv2.VideoCapture("ex1.mp4")

    while True:
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        results = model(frame, verbose=False)
        annotated = results[0].plot()
        cv2.line(annotated, (600, 0), (600, 1920), (0, 255, 0), 3)
        annotated = cv2.resize(annotated, (360, 640))

        _, buffer = cv2.imencode('.jpg', annotated)
        current_frame = base64.b64encode(buffer).decode('utf-8')
        print(f"프레임 저장됨: {len(current_frame)}")
        # YOLO 감지
       

        
        
 

        # 구역별 감지
        detected = {1: False, 2: False}
        for result in results:
            for box in result.boxes:
                if int(box.cls) == 0:  # person
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    for zone_id, zone in ZONES.items():
                        if is_person_in_zone((x1, y1, x2, y2), zone):
                            detected[zone_id] = True
                            print(f"{zone_id}번 런닝머신 사람 감지!")

        # state 업데이트
        for i in range(1, 3):
            if detected[i]:
                state.TREADMILL[i] = "/static/img/onhuman.png"
            else:
                state.TREADMILL[i] = "/static/img/offhuman.png"

        print("변경")