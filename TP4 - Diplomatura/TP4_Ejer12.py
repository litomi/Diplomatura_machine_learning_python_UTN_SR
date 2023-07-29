# 12. ¿En qué cree que puede consistir darle relieve a una imagen? Piense. Diseñe un kernel de
# 3x3 que considere debiera lograr un efecto de relieve en la imagen. Recuerde que los valores
# del kernel representan cuanta importancia se le dará o quitará a cada pixel vecino, y al
# pixel en cuestión del medio que se está calculando para la nueva imagen. Implemente un
# programa con dicho kernel y una imagen en escala de grises que usted elija. Experimente
# y muestre al profesor sus resultados :)

import cv2 as cv
import numpy as np

from Personal.funciones import *

kernel_1 = np.array([
    [-2, 0, 2],
    [-2, 0, 2],
    [-2, 0, 2]
], dtype='float')

kernel_2 = np.array([
    [2, 0, -2],
    [2, 0, -2],
    [2, 0, -2]
], dtype='float')


imagen = cv.imread('imagenes\\spider.jpeg')

imagen_gris = luma(imagen)

imagen_kernel_1 = convolucionar(imagen_gris, kernel_1)

imagen_kernel_2 = convolucionar(imagen_gris, kernel_2)

cv.imshow('Original', imagen)

cv.imshow('En Gris', imagen_gris)

cv.imshow('Filtrada kernel 1', imagen_kernel_1)

cv.imshow('Filtrada kernel 2', imagen_kernel_2)

cv.waitKey(0)

cv.destroyAllWindows()
