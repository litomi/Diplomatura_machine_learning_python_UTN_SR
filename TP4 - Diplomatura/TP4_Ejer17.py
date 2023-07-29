# 17. Crear una función rotar que tome dos argumentos: una imagen color y un ángulo de
# rotación. Devolvería una nueva imagen, que sería la original rotada dicho ángulo. El ángulo
# solo podría tomar los valores 90, 180, y 270. Generar una versión artesanal.

#[1][2][3] -> [3][6][9]
#[4][5][6] -> [2][5][8]  #90
#[7][8][9] -> [1][4][7]

#[1][2][3] -> [9][8][7]
#[4][5][6] -> [6][5][4] #180
#[7][8][9] -> [3][2][1]

#[1][2][3] -> [7][4][1]
#[4][5][6] -> [8][5][2] #270
#[7][8][9] -> [9][6][3]


import cv2 as cv
import numpy as np

from Personal.funciones import rotar

imagen = cv.imread('imagenes\\spider.jpeg')

cv.imshow('Original', imagen)

img_90 = rotar(imagen, 90)

img_180 = rotar(imagen, 180)

img_270 = rotar(imagen, 270)

cv.imshow('90', img_90)

cv.imshow('180', img_180)

cv.imshow('270', img_270)

cv.waitKey(0)

cv.destroyAllWindows()


