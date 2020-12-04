# Programa para procesar las imágenes de nubes
import numpy as np
# Biblioteca para leer imágenes y trabajar con ellas
import cv2
'''
Clase que tiene métodos para aplicar máscaras a una imagen.

@Author: Diego Velázquez, Mario Escobar
@Version: 1.0.0.

Métodos:

    a) Método para aplicar una máscara blanca a una imagen.
    b) Método para aplicar una máscara gris a una imagen.
'''
class MascarasRGB:

    '''
    Método para aplicar una máscara blanca
    @Param: Imagen (OpenCV)
    @Return: Regresa una máscara
    '''
    def mascarablanca(imagen):
        cota_inferior=np.array([np.round(215), np.round(220), np.round(220)])
        cota_superior=np.array([np.round(250), np.round(255), np.round(252)])
        return cv2.inRange(imagen,cota_inferior,cota_superior)
    '''
    Método para aplicar una máscara gris
    @Param: Imagen (OpenCV)
    @Return: Regresa una máscara
    '''
    def mascaragris(imagen):
        inferior=np.array([np.round(175), np.round(175), np.round(175)])
        superior=np.array([np.round(210), np.round(220), np.round(215)])
        return cv2.inRange(imagen,inferior,superior)
    '''
    Método para aplicar un bitwise a dos máscaras
    @Param: Máscara 1
    @Param: Máscara 2
    @Return: Máscara combinada
    '''
    def realiza_bit_wise(mascara1, mascara2):
            mascara_combinada = cv2.bitwise_or(mascara1,mascara2)
            return mascara_combinada
