from skimage import io, filters, feature
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
import cv2
import numpy as np

img = cv2.imread('./resources/nube.jpg')

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

# Para convertir a escala de grises:

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Gris', img_gris)
#cv2.imwrite('Grises.png',img_gris)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# Para mostrar los bordes de la imagen:

canny_edge = cv2.Canny(img, 30, 180)
sigma = 0.3
median = np.median(img)
lower = int(max(0, (1.0-sigma) * median))
upper = int(min(255, (1.0+sigma) * median))
auto_canny = cv2.Canny(img, lower, upper)

cv2.imshow("Original", img)
cv2.imshow("Canny", canny_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
