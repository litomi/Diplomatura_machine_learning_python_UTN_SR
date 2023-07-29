# 14. Generar dos imágenes del mismo tamaño, en blanco y negro, aleatorias (imagine ruido de
# TV). Determinar si son iguales o no. Probar con imágenes pequeñas primero, por ejemplo
# de 6 x 6 y luego imágenes de 500x600 pixeles. Utilizar la función Distancia de Hamming
# implementada anteriormente.

import cv2 as cv
import numpy as np
import random as ran
from TP3_Ejer13_HAMMING import hamming

base = 500
alto = 500

img1 = np.zeros((base, alto, 3), dtype= 'uint8')
img2 = np.zeros((base, alto, 3), dtype= 'uint8')

def cargar_ruido(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j] = ran.choice(((0, 0, 0), (255, 255, 255)))

cargar_ruido(img1)
cargar_ruido(img2)

cv.imshow('', img1)
cv.imshow('', img2)

cv.waitKey(0)

if (n:= hamming(img1.flat, img2.flat)) != -1:
    if n != 0:
        print("Difieren en {} elementos".format(n))
    else:
        print("Las imágenes son exactamente iguales.")
else:
    print("Las imágenes tienen diferente tamaño.")

