1. 라즈베리파이 GND부터 연결
2.흔들어서 뽑지말기


뺄떄는 파워먼저










가상환경 만들기
python -m venv venv
and python3 -m venv venv

가상환경 활성화
Windows:venv\Scripts\activate
Mac / Linux:source venv/bin/activate

패키지 파일(가상환경활성화 이후)
pip install fastapi uvicorn

[중요]깃에 푸쉬할때 가상환경venv와 yolo빼고 푸쉬해야 합니다. 
용량으로 깃안올라가거나 오래걸림 .gitignore에서 자동으로 제외설정했지만 만약 안된다면 다시확인해주세요 



실행 명령어 
웹사이트 활성화:uvicorn main:app --reload

실행명령어(메인):python main.py
코드로 unicorn명령어가 포함되어있습니다.

SMART_GYM

main.py에서 스레드분리로 3개로 기능마다 따로 실행됨니다.









# 🚀 FastAPI Project Setup Guide

## 🔹 Virtual Environment Setup

### Create a virtual environment

```bash
python -m venv venv
# or
python3 -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

## 🔹 Install Required Packages

*(after activating the virtual environment)*

```bash
pip install fastapi uvicorn
```

---

## 🔹 ⚠️ Important (Git Push)

* Do **NOT** include the `venv` folder or YOLO-related files when pushing to Git.
* They are too large and may cause upload failures or very slow pushes.
* These should already be excluded via `.gitignore`, but please double-check if needed.

---

## 🔹 Run the Server

```bash
python main.py
```

👉 This will start the FastAPI server.

---

## 🔹 Access the Website

* Main page:
  http://127.0.0.1:8000

* API docs (Swagger UI):
  http://127.0.0.1:8000/docs
