import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./CloudCoverageImgs/11840.JPG')
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# Elegimos el umbral de verde en HSV
umbral_bajo = (70,100,100)
umbral_alto = (80,255,255)
# hacemos la mask y filtramos en la original
mask = cv2.inRange(img_hsv, umbral_bajo, umbral_alto)
res = cv2.bitwise_and(img, img, mask=mask)

# imprimimos los resultados
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(res)
plt.show()
