# Biblioteca para procesar imágenes
import cv2
# Biblioteca para realizar operaciones matriciales
import numpy as np
# Biblioteca para realizar cálculos numéricos matemáticos
import math
'''
Clase que realiza una segmentación sobre una imagen previamente procesada.
La segmentación está orientada a identificar los pixeles del cielo en una nube
y los pixeles de nube.
@Author: Diego Velázquez, Mario Escobar
@Version: 1.0.0.
Métodos:
    a) Método de segmentación binaria.
    b) Método que obtiene el índice de cobertura nubosa.
'''
class IdentificadorNube:
    '''
    Método para obtener el área afuera de la circunferencia (negra)
    @Param: Dimensiones de la foto
    @Return: Área fuera de la circunferencia
    '''
    @staticmethod
    def areaFuera(dimensiones):
        radio = dimensiones[0]/2
        area_total = dimensiones[0] * dimensiones[1]
        area_circ  = math.pi * radio * radio
        return area_total - area_circ

    '''
    Método para hacer una segmentación binaria a una imagen preprocesada.
    @Param: Una imagen (CV2 OpenCV)
    @Return: Una imagen binaria en blanco y negro
    '''
    @staticmethod
    def procesa_imagen_nube(imagen):
        # Variables
        pixeles_negros = 0
        pixeles_blancos = 0
        pixel_dentro = False
        # Segmentación de la imagen
        for i in range(0,len(imagen)):

            for j in range(0, len(imagen[i])):
                if(imagen[i][j][0] == 0 and imagen[i][j][1] == 0 and imagen[i][j][2] == 0):
                    imagen[i][j] = 0
                    pixeles_negros += 1
                else:
                    imagen[i][j] = 255
                    pixeles_blancos += 1

        # Vamos a restarle los pixeles que están fuera de la circunferencia
        if(pixeles_negros > 0 and pixeles_blancos > 0):
            pixeles_negros = pixeles_negros - IdentificadorNube.areaFuera(imagen.shape)
        return (imagen, (pixeles_blancos)/(pixeles_negros+pixeles_blancos))
