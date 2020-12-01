# Programa para procesar las imágenes de nubes
import numpy as np
# Biblioteca para leer imágenes y trabajar con ellas
import cv2
# Biblioteca para leer el nombre del archivo
import sys
# Biblioteca para verificar si un archivo existe
import os.path
# Biblioteca para calcular el tiempo
import time


# Verificamos si el usuario ingresó la ruta de la imagen
if(len(sys.argv) < 2):
    print("USO :: -Imagen -Bandera (opcional)")
    sys.exit()

# Esta es la ruta relativa de la imagen
nombre_imagen = sys.argv[1]
if(len(sys.argv) == 3):
    bandera = sys.argv[2]

# Verificamos si existe el archivo con los datos
if(not os.path.isfile(nombre_imagen)):
    print("Imagen no encontrada")
    print("USO :: -Imagen -Bandera (opcional)")
    sys.exit()

# Leyendo la imagem
img = cv2.imread(nombre_imagen,1)

# Recortando la imagen
coord_x = int(img.shape[1]/2)
coord_y = int(img.shape[0]/2)
radius  = 1324
imageOut = img[coord_y-radius:coord_y+radius, coord_x-radius:coord_x+radius]

# Rescalar la imagen

#percent by which the image is resized
scale_percent = 30
#calculate the 50 percent of original dimensions
width = int(imageOut.shape[1] * scale_percent / 120)
height = int(imageOut.shape[0] * scale_percent / 120)
# dsize
dsize = (width, height)
# resize image
output = cv2.resize(imageOut, dsize)

# CLAHE Trabajo de disminución del contraste de la imagen
for i in range(1,2) :
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
    lab = cv2.cvtColor(output, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels
    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
    lab = cv2.merge((l2,a,b))  # merge channels
    output = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BG

imagenOriginalProcesada = output

cv2.imwrite('final.png', output)
output = cv2.imread('final.png')
img = output

YIQ = np.array([[0.299, 0.587, 0.114],
                [0.596, -0.275, -0.321],
                [0.212, -0.528, 0.311]])

# Esta es la matriz buena
YUV = np.array([[0.299, 0.587, 0.114],
                [-0.147, -0.289, 0.436],
                [0.615, -0.515, -0.100]])

CIE = np.array([[0.490, 0.310, 0.200],
                [0.177, 0.813, 0.011],
                [0, 0.010, 0.990]])

# Procesando los colores de la imagen para transformar a YUV
for i in range(0,len(img)):
    for j in range(0, len(img[i])):
        mat = np.array(img[i][j])
        img[i][j] = np.matmul(YIQ, mat)

# Aplicación de una máscara binaria
_, mask = cv2.threshold(img, thresh=180, maxval=255, type=cv2.THRESH_BINARY)
im_thresh_gray = cv2.bitwise_and(img, mask)

cv2.imshow("im_thresh_gray", im_thresh_gray)
cv2.imshow('Imagen PreFinal',img)
cv2.imshow('Imagen Procedente',imagenOriginalProcesada)
cv2.imwrite('prefinal.png', output)

# Segmentación de la imagen
for i in range(0,len(img)):
    for j in range(0, len(img[i])):
        if(im_thresh_gray[i][j][1] == 0 and im_thresh_gray[i][j][0] == 0):
            im_thresh_gray[i][j] = 0
        elif(im_thresh_gray[i][j][2] == 0 and im_thresh_gray[i][j][1] == 0 and im_thresh_gray[i][j][0] == 0):
            im_thresh_gray[i][j] = 255
        elif(im_thresh_gray[i][j][2] == 255 and im_thresh_gray[i][j][1] == 255 and im_thresh_gray[i][j][0] == 255):
            im_thresh_gray[i][j] = 255
        elif(im_thresh_gray[i][j][2] != 0 and im_thresh_gray[i][j][1] == 0 and im_thresh_gray[i][j][0] != 0):
            im_thresh_gray[i][j] = 255
        else:
            im_thresh_gray[i][j] = 255


cv2.imshow('Imagen Final',im_thresh_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
