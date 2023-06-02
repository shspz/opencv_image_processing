import cv2
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('더 이상 가져올 프레임이 없다.')
        break
    cv2.imshow('video', frame)

    if cv2.waitkey(1) == ord('q'):
        print('사용자 입력에 의해 종료합니다.')
        break

cap.release()
cv2.destroyAllWindows()