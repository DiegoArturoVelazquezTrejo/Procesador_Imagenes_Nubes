# Biblioteca para procesar imágenes
import cv2
# Biblioteca para realizar operaciones matriciales
import numpy as np
'''
Clase que tiene métodos para modificar todo lo relativo a dimensiones de una imagen.

@Author: Diego Velázquez, Mario Escobar
@Version: 1.0.0.

Métodos:

    a) Método para recortar una imagen.
    b) Método para reescalar una imagen.
'''
class ProcesaDimensiones:
    '''
    Método que realiza el recorte de una imagen en un subcuadrado menor, tomando en cuenta una
    circunferencia inscrita dentro de la imagen
    @Param: Radio de la circunferencia centrada en la imagen.
    @Param: Una imagen (CV2 OpenCV)
    @Return: imagen recortada
    '''
    @staticmethod
    def recorta_imagen(radio, imagen):
        # Recortando la imagen
        coord_x = int(imagen.shape[1]/2)
        coord_y = int(imagen.shape[0]/2)
        radius  = radio
        imageOut = imagen[coord_y-radius:coord_y+radius, coord_x-radius:coord_x+radius]
        return imageOut
    '''
    Método para reescalar una imagen.
    @Param: Porcentaje de reescalamiento.
    @Param: Una imagen (CV2 OpenCV)
    @Return: Imagen reescalada
    '''
    @staticmethod
    def reescala_iamgen(porcentaje, imagen):
        width = int(imagen.shape[1] * porcentaje / 120)
        height = int(imagen.shape[0] * porcentaje / 120)
        # dsize
        dsize = (width, height)
        # reescalando la imagen
        imagen = cv2.resize(imagen, dsize)
        return imagen
