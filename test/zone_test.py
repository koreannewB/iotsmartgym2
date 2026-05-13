import cv2

cap = cv2.VideoCapture("ex1.mp4")
ret, frame = cap.read()

# 구역 선 그리기
cv2.line(frame, (600, 0), (600, 1920), (0, 255, 0), 3)
cv2.putText(frame, "1번", (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 3)
cv2.putText(frame, "2번", (700, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 3)

cv2.imwrite("zone_check.jpg", frame)
print("zone_check.jpg 저장완료!")
cap.release()