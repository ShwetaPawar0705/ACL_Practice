import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('panda.jpg')

denoise = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)

plt.subplot(121), plt.imshow(image)
plt.subplot(122), plt.imshow(denoise)

plt.show()