# Programa para procesar las imágenes de nubes
import numpy as np
# Biblioteca para leer imágenes y trabajar con ellas
import cv2
# Biblioteca para leer el nombre del archivo
import sys
# Biblioteca para verificar si un archivo existe
import os.path
# Biblioteca para graficar información
from matplotlib import pyplot as plt

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
img = cv2.imread(nombre_imagen)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
output = cv2.resize(imageOut, dsize)


cv2.imshow('Imagen de salida',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

TP= width * height
white= TP - cv2.countNonZero(img[1])
print("Dimensions:", imageOut.size, "Total pixels:", TP, "White", white)


# Proceso de segmentación
#definimos que pixel es de cielo O que pixel es de nube
#Iteramos y seguimos contando pixeles
#calculamos el indice
#si el usuario paso la badnera s guardamos la imagen segmenetada

# Calcular el índice de nubosidad
'''

Idea de como deshacernos de los pixeles que están fuera de la circunferencia de la fotografía del cielo.

Idea 1: De la imagen recortada, contamos la cantidad de pixeles negros, esa cantidad de pixeles negros
considera los pixeles negros que están fuera de la circunferencia más los pixeles negros de la imagen (de la circunferencia).
Calculamos el área del rectángulo de la imagen recortada menos el área del círculo y esa diferencia nos darán los pixeles negros
afuera de la circunferencia. Tomamos la cantidad de pixeles negros en total y le restamos los pixeles negros de afuera del círculo y
ese número será el total de pixeles negros dentro de la circunferencia (considerando que está segmenetada).

'''
