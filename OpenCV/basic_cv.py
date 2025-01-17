# Read Images

import cv2

image = cv2.imread('road.jpg')

cv2.imshow('Road', image)
cv2.waitKey(0)

# Read Videos
capture = cv2.VideoCapture('/home/shweta/Documents/CV/animal.mp4')

while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(20) & 0xFF == ord('d'):
            break
capture.release()
cv2. destroyAllWindows()