import cv2
import matplotlib.pyplot as plt

image= cv2.imread('road.jpg')

# Gray Scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray_Scale', gray)


# Blur
blur = cv2.GaussianBlur(image, (3,3), cv2.BORDER_DEFAULT)
cv2.imshow('Blur',blur)

# Canny Edge Detection
canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny Edges',canny)

# Dilating the image
dilated = cv2.dilate(canny, (7,7), iterations=3)
cv2.imshow('Dilated', dilated)

# Eroding
eroded = cv2.erode(dilated, (7,7), iterations=3)
cv2.imshow('Eroded', eroded)

# Resize
resized = cv2.resize(image, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

# Cropping
cropped = image[100:200, 200:300]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)