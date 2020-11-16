import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('coins.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)


cv.imshow('coins', img)
cv.waitKey(0)
cv.destroyAllWindows()
