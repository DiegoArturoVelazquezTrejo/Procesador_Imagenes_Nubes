# Biblioteca para procesar imágenes
import cv2
# Biblioteca para realizar operaciones matriciales
import numpy as np
# Biblioteca para realizar cálculos numéricos matemáticos
import math
'''
Clase que contiene métodos para procesar los colores de una imagen
@Author: Diego Velázquez, Mario Escobar
@Version: 1.0.0.

Métodos:

    a) Método para disminuir el contraste de una imagen.
    b) Método para cambiar los colores de RGB a YIQ.
    c) Método para aplicar thresholding.
    d) Método para la corrección de la iluminación en una imagen.
    e) Método para la corrección de la iluminación en una imagen (alternativa).
    f) Método para convertir a HSL.

'''
class ProcesaImagen:

    @staticmethod
    def convierte_rgb(imagen):
        return cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    '''
    Método para disminuir el contraste de una imagen
    @Param: Número de veces que se le aplica el contraste a la imagen.
    @Param: Una imagen (CV2 OpenCV)
    @Return: Imagen con el contraste disminuido
    '''
    @staticmethod
    def disminuir_contraste(numero, imagen):
        for i in range(0,numero) :
            clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))
            lab = cv2.cvtColor(imagen, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
            l, a, b = cv2.split(lab)  # split on 3 different channels
            l2 = clahe.apply(l)  # apply CLAHE to the L-channel
            lab = cv2.merge((l2,a,b))  # merge channels
            imagen = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BG
        return imagen
    '''
    Método para cambiar los colores de RGB a YUV utilizando multiplicación matricial
    @Param: Una imagen (CV2 OpenCV)
    @Return: Imagen en escala YUV.
    '''
    @staticmethod
    def convierte_yiq(imagen):
        # Esta es la matriz de la transformación lineal a YUV
        YUV = np.array([[0.299, 0.587, 0.114],
                        [-0.147, -0.289, 0.436],
                        [0.615, -0.515, -0.100]])
        # Esta es la matriz de trasnformación lineal a YIQ
        YIQ = np.array([[0.299, 0.587, 0.114],
                        [0.596, -0.275, -0.321],
                        [0.212, -0.528, 0.311]])
        # Procesando los colores de la imagen para transformar a YUV
        for i in range(0,len(imagen)):
            for j in range(0, len(imagen[i])):
                mat = np.array(imagen[i][j])
                imagen[i][j] = np.matmul(YIQ, mat)
        return imagen
    '''
    Método para cambiar los colores de RGB a HSL
    @Param: Una imagen (CV2 OpenCV)
    @Return: Imagen en espacio de color HSL.
    '''

    @staticmethod
    def convierte_hls(imagen):
        return cv2.cvtColor(imagen, cv2.COLOR_BGR2HLS)


    '''
    Método para cambiar los colores de RGB a HSV
    @Param: Una imagen (CV2 OpenCV)
    @Return: Imagen en espacio de color HSL.
    '''
    @staticmethod
    def convierte_hsv(imagen):
        return  cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)


    '''
    Método para aplicar un threshold primario binario a una imagen
    @Param: Una imagen (CV2 OpenCV)
    @Return: imagen con el threshold aplicado
    '''
    @staticmethod
    def aplica_threshold(imagen):
        _, mask = cv2.threshold(imagen, thresh=180, maxval=255, type=cv2.THRESH_BINARY)
        im_thresh_gray = cv2.bitwise_and(imagen, mask)
        return im_thresh_gray
    '''
    Método que realiza una corrección gamma sobre la imagen. Corrección de luz en la imagen.
    @Param: Una imagen (CV2 OpenCV)
    @Return: Una imagen más nítida
    '''
    @staticmethod
    def realiza_corr_gama_1(imagen):
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        mid = 0.5
        mean = np.mean(gray)
        gamma = math.log(mid*255)/math.log(mean)
        # gamma correction
        imagen = np.power(imagen, gamma).clip(0,255).astype(np.uint8)
        return imagen
    '''
    Método que realiza una corrección de la iluminación en una imagen, alternativa.convirtiendo la imagena  hsv
    @Param: Una imagen (CV2 OpenCV)
    @Return: Una imagen en donde la luz blanca deja de ser tan intensa.
    '''
    @staticmethod
    def realiza_corr_gama_2(imagen):
        hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
        hue, sat, val = cv2.split(hsv)
        mid = 0.5
        mean = np.mean(val)
        gamma = math.log(mid * 255)/math.log(mean)
        val_gamma = np.power(val, gamma).clip(0,255).astype(np.uint8)
        # se combina el nuevo valor con hue y sat canales
        hsv_gamma = cv2.merge([hue, sat, val_gamma])
        imagen = cv2.cvtColor(hsv_gamma, cv2.COLOR_HSV2BGR)
        return imagen
    '''
    Método para aplicarle una máscara a una imagen
    @Param: Máscara
    @Param: Imagen (OpenCV)
    @Return: imagen
    '''
    def aplica_mascar_img(mascara, imagen):
        mascara_aplicada = cv2.bitwise_and(imagen, imagen, mask = mascara)
        return mascara_aplicada
