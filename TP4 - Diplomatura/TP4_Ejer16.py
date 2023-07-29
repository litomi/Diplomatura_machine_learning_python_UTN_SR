# 16. Implementar una función llamada mascara que tome 3 argumentos: una imagen, y dos
# tuplas BGR que representarán un rango de color, y que genere una imagen en blanco
# y negro, de mismo tamaño que la original, tal que si el pixel en la imagen original se
# encuentra en el rango de color dado, la imagen mascara tendrá el color blanco en ese
# pixel, y sino tendrá el color negro en ese pixel.

import cv2 as cv
import numpy as np

def mascara(imagen, r1, r2):
    nueva = np.zeros(imagen.shape, dtype='uint8')
    for i in range(len(imagen)):
        for j in range(len(imagen[0])):
            if (imagen[i, j] >= r1).all() and  (imagen[i, j] <= r2).all():
                nueva[i, j] = (0, 0, 0)
            else:
                nueva[i, j] = (255, 255, 255)
    return nueva

imagen = cv.imread('imagenes\\spider.jpeg')

cv.imshow('Original', imagen)

img_byn = mascara(imagen, (120, 120, 120), (150, 150, 150))

cv.imshow('Con máscara', img_byn)

cv.waitKey(0)

cv.destroyAllWindows()



