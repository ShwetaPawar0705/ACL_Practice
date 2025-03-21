import cv2
import numpy as np

image1 = cv2.imread('panda.jpg')

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
                             cv2.THRESH_OTSU)

cv2.imshow('Otsu Threshold', thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()