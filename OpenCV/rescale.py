import cv2

# image = cv2.imread('road.jpg')

# cv2.imshow('Road', image)

def rescaleFrame(frame, sclae=0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

capture = cv2.VideoCapture('/home/shweta/Documents/CV/animal.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame)
    cv2.imshow('Video', frame)
    cv2.imshow('Video Resized', frame_resize)
    if cv2.waitKey(20) & 0xFF == ord('d'):
            break
capture.release()
cv2. destroyAllWindows()
cv2.waitKey(0)