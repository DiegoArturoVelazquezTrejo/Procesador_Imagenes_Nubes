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


# CLAHE (Contrast Limited Adaptive Histogram Equalization)
for i in range(1,2) :
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
    lab = cv2.cvtColor(output, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels
    l2 = clahe.apply(l)  # apply CLAHE to the L-channel
    lab = cv2.merge((l2,a,b))  # merge channels
    output = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BG

imagenOriginalProcesada = output

#cv2.imwrite('final.png', output)

# Aquí viene nuestro desmadre

output3 = cv2.applyColorMap(output, cv2.COLORMAP_OCEAN)
output = cv2.applyColorMap(output3, cv2.COLORMAP_HOT)
output = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)

'''
Aquí vamos a iterar sobre cada pixel de la imagen y otenemos un pixelPromedio con peso, que resulta de
sumar la entrada iésima del pixel jésimo de la imagen origina (Mario) multiplicada por un peso y la entrada iésima
del pixel jésimo de la imagen final (grises), dividir entre dos la entrada iésima del pixelPromedio y posteriormente
calcular la distancia euclediana con respecto al pixel bñanco (255, 255, 255) y el pixel negro (0,0,0)
La mínima distancia será la que indique la clase a la que el pixel pertenece


# Imrpimiendo resultados
print("Distancia con respecto al blanco")
print(distancia(tfp, tb))
print("Distancia con respecto al negro")
print(distancia(tfp, tn))
'''

# Función que regresa la distancia euclediana
def distancia(tupla1, tupla2):
    return math.sqrt( math.pow(tupla2[0]-tupla1[0], 2) + math.pow(tupla2[1]-tupla1[1], 2) + math.pow(tupla2[2]-tupla1[2], 2)   )

# Función que calcula el promedio de los pixeles
def promedio(pixeles):
    return (pixeles[0] + pixeles[1] + pixeles[2])/3

# Función que estudia el rango de los pixeles RGB
def estudiaRangoPixeles(pixeles):
    return (pixeles[0] > 125 and pixeles[1] > 125 and pixeles[2] > 125)

# Función para determinar la clasificación del pixel
# True para indicar que el pixel es negro
# False para indicar que el pixel es blanco
def clasificaPixel(pixelGris, pixelNormal1, pesoImportancia):


    # Definimos las tuplas dominantes
    b = [255, 255, 255]
    n = [1, 1, 1]

    pixelNormal1 = [pesoImportancia*pixelNormal1[0], pesoImportancia*pixelNormal1[1], pesoImportancia*pixelNormal1[2]]
    # Aquí reside el problema
    tp = (pixelGris[0]+pixelNormal1[0], pixelGris[1]+pixelNormal1[1], pixelGris[2]+pixelNormal1[2])
    tfp = (tp[0]/(1+pesoImportancia), tp[1]/(1+pesoImportancia), tp[2]/(1+pesoImportancia))

    if(distancia(b, tfp) < distancia(n, tfp)):
        return False
    else:
        return True

cv2.imwrite('final.png', output)
output = cv2.imread('final.png')
cv2.imshow('Imagen pre procesada', output)

print(output[242][580])
print(imagenOriginalProcesada[242][580])

for i in range(0, len(output)):
    for j in range(0, len(output[0])):
        #if(clasificaPixel(output[i][j], imagenOriginalProcesada[i][j], 0.95)):
        if(promedio(output[i][j]) > 180):
            output[i][j] = [255,255,255]
        elif(promedio(output[i][j]) < 30):
            output[i][j] = [0,0,255]
        elif(promedio(output[i][j]) < 100 and promedio(imagenOriginalProcesada[i][j]) > 100):
            output[i][j] = [0,0,255]
        else:
            output[i][j] = [255,255,255]

#output = cv2.imread('final.png')

cv2.imshow('Imagen original',imagenOriginalProcesada)
cv2.imwrite('original.png', imagenOriginalProcesada)
#TP= width * height
#white= TP - cv2.countNonZero(img[1])
#print("Dimensions:", output.size, "Total pixels:", TP, "White", white)

cv2.imshow('Imagen Final',output)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
 Idea para eliminar los pixeles negros fuera de la circunferencia
 que no pertenecen a la imagen tomada


 Idea 1: De la imagen recortada, contamos la cantidad de pixeles negros, esa cantidad de pixeles negros
 considera los pixeles negros que están fuera de la circunferencia más los pixeles negros de la imagen (de la circunferencia).
 Calculamos el área del rectángulo de la imagen recortada menos el área del círculo y esa diferencia nos darán los pixeles negros
 afuera de la circunferencia. Tomamos la cantidad de pixeles negros en total y le restamos los pixeles negros de afuera del círculo y
 ese número será el total de pixeles negros dentro de la circunferencia (considerando que está segmenetada).
'''
