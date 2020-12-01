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
    Método para calcular la distancia euclediana del centro de la circunferencia.
    @Param: (x,y)
    @Param: Radio de la circunferencia
    @Return True si el punto está dentro, False de lo contrario.
    '''
    @staticmethod
    def distancia_euclediana(vector, centro):
        return math.sqrt( math.pow(vector[0] - centro[0],2)+ math.pow(vector[1] - centro[1],2)) <= centro[0]
    '''
    Método para hacer una segmentación binaria a una imagen preprocesada.
    @Param: Una imagen (CV2 OpenCV)
    @Return: Una imagen binaria en blanco y negro
    '''
    @staticmethod
    def procesa_imagen_nube(imagen, centro):
        # Variables
        pixeles_negros = 0
        pixeles_blancos = 0
        pixel_dentro = False
        # Segmentación de la imagen
        for i in range(0,len(imagen)):
            for j in range(0, len(imagen[i])):
                # Verificar que la coordenada (i,j) esté dentro de la circunferencia, si sí está, consideramos la suma de blanco o negro.
                pixel_dentro =  IdentificadorNube.distancia_euclediana([i,j], centro)
                if(imagen[i][j][1] == 0 and imagen[i][j][0] == 0):
                    imagen[i][j] = 0
                    if(pixel_dentro):
                        pixeles_negros += 1
                elif(imagen[i][j][2] == 0 and imagen[i][j][1] == 0 and imagen[i][j][0] == 0):
                    imagen[i][j] = 255
                    if(pixel_dentro):
                        pixeles_blancos += 1
                elif(imagen[i][j][2] == 255 and imagen[i][j][1] == 255 and imagen[i][j][0] == 255):
                    imagen[i][j] = 255
                    if(pixel_dentro):
                        pixeles_blancos += 1
                elif(imagen[i][j][2] != 0 and imagen[i][j][1] == 0 and imagen[i][j][0] != 0):
                    imagen[i][j] = 255
                    if(pixel_dentro):
                        pixeles_blancos += 1
                else:
                    imagen[i][j] = 255
                    if(pixel_dentro):
                        pixeles_blancos += 1
        #print("Área del círculo: ", (pixeles_negros+pixeles_blancos))
        #print("Pixeles blancos: ", pixeles_blancos)
        #print("Pixeles negros: ", pixeles_negros)
        return (imagen, (pixeles_blancos)/(pixeles_negros+pixeles_blancos))
