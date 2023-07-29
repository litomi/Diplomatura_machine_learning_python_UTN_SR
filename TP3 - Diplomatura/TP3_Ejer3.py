# 3. Crear una imagen del tamaño que desee, que tenga un arcoiris
# de 6 colores, organizada en 6 grandes rayas horizontales.

import cv2 as cv
import numpy as np

marco = np.zeros((450, 720, 3), dtype='uint8')
colores = (
    (211, 0, 148),
    (130, 0, 75),
    (255, 0, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 127, 255)
)

def dibujarRectangulo(marco, colores):
    franjas = len(colores)
    for i in range(franjas):
        incio = (0, int(len(marco) / franjas) * i)
        fin = (len(marco[0]), int(len(marco) / franjas) * (i + 1))
        color = colores[i]
        imagen = cv.rectangle(marco, incio, fin, color, -1)
    return imagen

imagen = dibujarRectangulo(marco, colores)

cv.imwrite("imagenes/ejer3.jpg", imagen)

cv.imshow('franjas', imagen)

cv.waitKey(0)
