import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('image.jpeg')

mask = np.zeros(image.shape[:2], np.uint8)

backgroundModel = np.zeros((1, 65), np.float64)
foregroundModel = np.zeros((1, 65), np.float64)

recctangle = (20,100,200,200)

cv2.grabCut(image, mask, recctangle, backgroundModel, foregroundModel, 3, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask == 0), 0, 1).astype('uint8')

image_segmented = image * mask2[:, :, np.newaxis]

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image_segmented, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Segmented Image')
plt.imshow(cv2.cvtColor(image_segmented, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
