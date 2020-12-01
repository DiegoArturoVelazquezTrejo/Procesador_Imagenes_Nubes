# import opencv
import cv2
# Read image
src = cv2.imread("./resources/nube.jpg", cv2.IMREAD_GRAYSCALE)
# Set threshold and maxValue
thresh = 0
maxValue = 255
# Basic threshold example
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)

cv2.imshow("Image", src)
cv2.waitKey(0)
