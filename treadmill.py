import time
from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
import state
from ultralytics import YOLO



model = YOLO('yolov8n.pt')
# 각 구역별 타이머 (여기서는 2번만 예시)
box_timers = {1: None, 2: None, 3: None, 4: None}

def trail_detect_run():
    print("런닝머신감지기능작동")
    #조건 넣는 구간!!!!
    print(state.TREADMILL[1])
    #지정 
    condition = {1: False, 2: True, 3: True, 4: True}
    


    while True:
    # 카메라에서 프레임 읽기 (예시에서는 비디오 파일 사용)
    # 현제는 테스트용으로 1,3,4번구역 사용중 2번자리 비어있음
    #
    #
    #
        for i in range(1, 5):
            if condition[i]:
                state.TREADMILL[i] = "/static/img/onhuman.png"
            else:
                state.TREADMILL[i]= "/static/img/offhuman.png"
            
        time.sleep(1)
        print("변경")
        
        if condition[1] == False:
            condition[1] = True
        else:
            condition[1] = False



       
