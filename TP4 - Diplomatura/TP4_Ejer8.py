# 8. Implementar una función que genere una imagen binaria invertida, dada una imagen en
# escala de grises y un valor de umbral, pasados como argumentos. Por ejemplo, para la
# imagen fordt:png se podría apreciar la versión binaria esándar a la izquierda, y la versión
# binaria invertida a la derecha.

from Personal.funciones import *
import matplotlib.pyplot as plt
import cv2 as cv

imagen = cv.imread('imagenes\\actriz.png')

imagen_gris = luma(imagen)

imagen_binaria = bn(imagen_gris, 90)

imagen_invertida = binaria_invertida(imagen_gris, 90)

cv.imshow('Original', imagen)

cv.imshow('En grises', imagen_gris)

cv.imshow('Binaria Invertida', imagen_invertida)

cv.imshow('Binaria', imagen_binaria)

cv.waitKey(0)

cv.destroyAllWindows()