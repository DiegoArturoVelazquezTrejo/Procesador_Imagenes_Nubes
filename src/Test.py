# Biblioteca para leer y trabajar con imágenes
import cv2
# Biblioteca de métodos para procesar imágenes de nubes
from IdentificadorNube import IdentificadorNube as idn
# Biblioteca para procesar las imágenes (colores)
from ProcesaImagen import ProcesaImagen as pi
# Biblioteca para procesar las dimensiones de imágenes
from ProcesaDimensiones import ProcesaDimensiones as pdim
# Biblioteca para realizar cálculos numéricos matemáticos
import math
'''
Clase para realizar las prebas unitarias
'''


#Método para probar que se realice el conteo de los pixeles blancos
def prueba_conteo_pixeles_blancos():
    # Vamos a leer una imagen blanca completamente
    imagen = cv2.imread('src/pruebas/blanco.png')
    filas, columnas, canales = imagen.shape
    total_pixeles_blancos = filas * columnas
    imagen, indice = idn.procesa_imagen_nube(imagen)
    return indice == 1

#Método para probar que se realice el conteo de los pixeles blancos
def prueba_conteo_pixeles_negros():
    # Vamos a leer una imagen blanca completamente
    imagen = cv2.imread('src/pruebas/negro.jpg')
    filas, columnas, canales = imagen.shape
    total_pixeles_blancos = filas * columnas
    imagen, indice = idn.procesa_imagen_nube(imagen)
    return indice == 1
#Método para corroborar que se recorte adecuadamente una imagen
def prueba_recorte_imagen():
    # Vamos a leer una imagen blanca completamente
    imagen = cv2.imread('src/pruebas/blanco.png')
    filas, columnas, canales = imagen.shape
    radio = 100
    imagen = pdim.recorta_imagen(radio, imagen)
    return imagen.shape[0] == (filas/2)

#Método para verificar el conteo de pixeles blancos y negros
def prueba_blanco_negro():
    # Vamos a leer una imagen blanca completamente
    imagen = cv2.imread('src/pruebas/circulo.jpg')
    filas, columnas, canales = imagen.shape
    areaCircInscrita = (626/2) * (626/2) * math.pi
    indiceP = 317220 / areaCircInscrita
    imagen, indice = idn.procesa_imagen_nube(imagen)
    return indice == indiceP

if(prueba_conteo_pixeles_blancos()):
    print("Prueba de conteo de pixeles blancos completada .... 100%")
if(prueba_conteo_pixeles_negros()):
    print("Prueba de conteo de pixeles negros  completada .... 100%")
if(prueba_recorte_imagen()):
    print("Prueba de recorte de una   imagen   completada .... 100%")
if(prueba_blanco_negro()):
    print("Prueba de conteo de pixeles b y n   completada .... 100%")
