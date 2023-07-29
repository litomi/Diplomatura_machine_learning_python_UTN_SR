# 14. Implemente un programa que ejecute el filtro Gaussiano de 3x3 de suavizado en una
# imagen color de 3 canales. ¿Qué piensa debería hacer para adaptar el algoritmo con
# imagenes de escala de grises, a una imagen color?

import cv2 as cv
import numpy as np
from Personal.funciones import *

# imagen = cv.imread('imagenes\\perrito.jpg')
imagen = cv.imread('imagenes\\spider.jpeg')


imagen_1 = imagen.copy()

kernel = np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]], dtype='float')/16

kernel_1 = np.array([
    [1, 4, 7, 4, 1],
    [4, 16, 26, 16, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 26, 16, 4],
    [1, 4, 7, 4, 1]
], dtype='float') / 256

def convolucionar3C(imagen, kernel):
    nueva = imagen.copy()
    for i in range(3):
        nueva[:, :, i] = convolucionar(imagen[:, :, i], kernel)
    return nueva

imagen_1 = convolucionar3C(imagen, kernel)

imagen_2 = convolucionar3C(imagen, kernel_1)




cv.imshow('Original', imagen)

cv.imshow('Filtrado 3x3', imagen_1)

cv.imshow('Filtrado 5x5', imagen_2)


cv.waitKey(0)

cv.destroyAllWindows()

