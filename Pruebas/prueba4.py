
import cv2
import numpy as np
from matplotlib import pyplot as plt




img = cv2.imread('./resources/nube.jpg', cv2.IMREAD_GRAYSCALE)

# Recortar la imagen
coord_x = int(img.shape[1]/2)
coord_y = int(img.shape[0]/2)
radius  = 1324
imageOut = img[coord_y-radius:coord_y+radius, coord_x-radius:coord_x+radius]


# Rescalar la imagen

#percent by which the image is resized
scale_percent = 20
#calculate the 50 percent of original dimensions
width = int(imageOut.shape[1] * scale_percent / 120)
height = int(imageOut.shape[0] * scale_percent / 120)
# dsize
dsize = (width, height)
# resize image
img = cv2.resize(imageOut, dsize)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
