# python app.py
# 가상환경 source venv/bin/activate 



import treadmill
import towel_remaining
import fitness_equipment
import state
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import time
import threading
import uvicorn

from fastapi.staticfiles import StaticFiles
    
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



    # 이파일실행될떄만 실행되도록 
@app.get('/')
async def index():
    return FileResponse('templates/index.html')
@app.get("/TMdata")
async def tm_data():
    return {
        "Tmn1": state.TREADMILL[1],
        "Tmn2": state.TREADMILL[2],
        "Tmn3": state.TREADMILL[3],
        "Tmn4": state.TREADMILL[4]
    }

def main():
        
    #sensor.init_gpio()
    #sensor.start_threads()

    # 각 기능 3개가 동시에 작동하도록 스레드생성
    threadtreadmill = threading.Thread(target=treadmill.trail_detect_run)
    # threadtowel = threading.Thread(target=towel_remaining.run)
    # threadfitness = threading.Thread(target=fitness_equipment.run)

    threadtreadmill.daemon = True
    # threadtowel.daemon = True
    # threadfitness.daemon = True

    threadtreadmill.start()
    # threadtowel.start()
    # threadfitness.start()

    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()


    