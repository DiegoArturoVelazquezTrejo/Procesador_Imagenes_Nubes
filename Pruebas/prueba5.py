import cv2
import numpy as np

img = cv2.imread("./resources/nube.jpg", cv2.IMREAD_GRAYSCALE)

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

_, threshold_binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
_, threshold_binary_inv = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
_, threshold_trunc = cv2.threshold(img, 128, 255, cv2.THRESH_TRUNC)
_, threshold_to_zero = cv2.threshold(img, 12, 255, cv2.THRESH_TOZERO)

cv2.imshow("Image", img)
cv2.imshow("th binary", threshold_binary)
cv2.imshow("th binary inv", threshold_binary_inv)
cv2.imshow("th trunc", threshold_trunc)
cv2.imshow("th to zero", threshold_to_zero)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np


cv2.namedWindow("Image")
cv2.createTrackbar("Threshold value", "Image", 128, 255, nothing)

while True:
    value_threshold = cv2.getTrackbarPos("Threshold value", "Image")
    _, threshold_binary = cv2.threshold(img, value_threshold, 255, cv2.THRESH_BINARY)
    _, threshold_binary_inv = cv2.threshold(img, value_threshold, 255, cv2.THRESH_BINARY_INV)
    _, threshold_trunc = cv2.threshold(img, value_threshold, 255, cv2.THRESH_TRUNC)
    _, threshold_to_zero = cv2.threshold(img, value_threshold, 255, cv2.THRESH_TOZERO)
    _, threshold_to_zero_inv = cv2.threshold(img, value_threshold, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow("Image", img)
    cv2.imshow("th binary", threshold_binary)
    cv2.imshow("th binary inv", threshold_binary_inv)
    cv2.imshow("th trunc", threshold_trunc)
    cv2.imshow("th to zero", threshold_to_zero)
    cv2.imshow("th to zero inv", threshold_to_zero_inv)

key = cv2.waitKey(100)


cv2.destroyAllWindows()
