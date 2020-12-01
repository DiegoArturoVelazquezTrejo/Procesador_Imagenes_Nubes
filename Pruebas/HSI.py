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
# Biblioteca de matemáticas
import math
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

# Función que regresa el mínimo
def min1(pixel):
    return min(pixel[0], pixel[1], pixel[2])

# Ecuación de transformación
def transformacion_H(pixel):
    num = pixel[0]
    den = math.sqrt(math.pow((pixel[0] - pixel[1]), 2) + (pixel[0] - pixel[2])*(pixel[1]-pixel[2]))
    if(den == 0):
        den = 1
    print(num/den)
    return math.acos(num/den)
def transformacion_S(pixel):
    return 1 - (3/(pixel[0]+pixel[1]+pixel[2]))*min1(pixel)
def transformacion_I(pixel):
    return (1/3)*(pixel[0]+pixel[1]+pixel[2])

for i in range(0,len(img)):
    for j in range(0, len(img[i])):
        mat = np.array([transformacion_H(img[i][j]), transformacion_S(img[i][j]),transformacion_I(img[i][j])])
        img[i][j] = mat


img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



cv2.imshow('Imagen Final',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
