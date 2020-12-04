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
from PIL import Image
# Importamos las biblioteca que diseñamos para el procesado de imágenes

# Biblioteca de métodos para procesar imágenes de nubes
from IdentificadorNube import IdentificadorNube as idn
# Biblioteca para procesar las imágenes (colores)
from ProcesaImagen import ProcesaImagen as pi
# Biblioteca para procesar las dimensiones de imágenes
from ProcesaDimensiones import ProcesaDimensiones as pdim
# Biblioteca de métodos para trabajar con máscaras
from MascarasRGB import MascarasRGB as mrgb

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

# Verificamos el formato de la imagen
if(not nombre_imagen.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
    print("Formato de la imagen inválido ... ")
    sys.exit()

# Leyendo la imagen
imagen = cv2.imread(nombre_imagen,1)

# Verificar que la imagen sea de las dimensiones que buscamos
filas, columnas, canales = imagen.shape
if(columnas != 4368  and  filas != 2912):
    print("\nLas dimensiones de la imagen tienne que ser 4368 de largo y 2912 de ancho")
    sys.exit()

# Definimos el tamaño del radio de la imagen
radio_imagen = 1324
# Convertimos la imagen a rgb
imagen=pi.convierte_rgb(imagen)

# Recortamos la imagen en un cuadrado con la circunferencia centrada
imagen = pdim.recorta_imagen(radio_imagen, imagen)

# Reescalamos la imagen en un 30%
imagen=pdim.reescala_iamgen(30,imagen)

# Realizamos una corrección gamma de iluminación a la imagen
#imagen = pi.realiza_corr_gama_2(imagen)

# Realizamos el procesado de la imagen
#imagen = pi.disminuir_contraste(1, imagen)

#imagen =pi.convierte_hls(imagen)

# Realizamos la transformación YUV
#imagen=pi.convierte_hls(imagen)

# Aquí obtenemos las máscaras
mascara_blanca = mrgb.mascarablanca(imagen)
mascara_gris  = mrgb.mascaragris(imagen)

# Obtenemos una máscara combinando las dos anteriores
mascara_combinada = mrgb.realiza_bit_wise(mascara_blanca, mascara_gris)

# Aplicarle la máscara general a la imagen
imagen = pi.aplica_mascar_img(mascara_combinada, imagen)

# Realizamos la aplicación de la máscara binaria
imagen = pi.aplica_threshold(imagen)

# Realizamos la segmentación binaria de la imagen
imagen, indice = idn.procesa_imagen_nube(imagen)

# Imprimimos el índice
print("El índice de cobertura nubosa es: ", indice)

# Mostramos la imagen
if(bandera != None):
    cv2.imshow('Imagen Final', imagen)
    nom_final = "-seg"+nombre_imagen
    cv2.imwrite(nom_final, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
