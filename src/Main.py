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

# Importamos las biblioteca que diseñamos para el procesado de imágenes

# Biblioteca de métodos para procesar imágenes de nubes
from IdentificadorNube import IdentificadorNube as idn
# Biblioteca para procesar las imágenes (colores)
from ProcesaImagen import ProcesaImagen as pi
# Biblioteca para procesar las dimensiones de imágenes
from ProcesaDimensiones import ProcesaDimensiones as pdim

# Verificamos si el usuario ingresó la ruta de la imagen
if(len(sys.argv) < 2):
    print("USO :: -Ruta-Imagen -Bandera (opcional)")
    sys.exit()

# Esta es la ruta relativa de la imagen
nombre_imagen = sys.argv[1]
bandera = None 
if(len(sys.argv) == 3):
    bandera = sys.argv[2]

# Verificamos si existe el archivo con los datos
if(not os.path.isfile(nombre_imagen)):
    print("Imagen no encontrada")
    print("USO :: -Ruta-Imagen -Bandera (opcional)")
    sys.exit()

# Leyendo la imagem
img = cv2.imread(nombre_imagen,1)
# Definimos el tamaño del radio de la imagen
radio_imagen = 1324

# Primero recortamos la imagen
imagen = pdim.recorta_imagen(radio_imagen, img)
# Reescalamos la imagen
imagen = pdim.reescala_iamgen(30, imagen)
# Realizamos una corrección gamma de iluminación a la imagen
imagen = pi.realiza_corr_gama_1(imagen)
# Realizamos el procesado de la imagen
imagen = pi.disminuir_contraste(1, imagen)
if(bandera != None):
    cv2.imshow('Imagen Original', imagen)
# Realizamos la transformación YUV
imagen = pi.convierte_yiq(imagen)
if(bandera != None):
    cv2.imshow('Imagen escala YIQ', imagen)
# Realizamos la aplicación de la máscara binaria
imagen = pi.aplica_threshold(imagen)
# Realizamos la segmentación binaria de la imagen
imagen, indice = idn.procesa_imagen_nube(imagen, [len(imagen)/2, len(imagen)/2])
# Imprimimos el índice
print("El índice de cobertura nubosa es: ", indice)

# Mostramos la imagen
if(bandera != None):
    cv2.imshow('Imagen Final', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
