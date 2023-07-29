# 7. Con la imagen binaría generada en el punto anterior, utilicela como una máscara para
# recortar la actriz del fondo, y generar una imagen nueva, que tenga la actriz sobre un
# fondo anaranjado por ejemplo. Podrá observar fácilmente, el desafío presente en separar figura de fondo.

import cv2 as cv
import numpy as np

mascara = cv.imread('imagenes\\actriz_bicolor.png')
imagen = cv.imread('imagenes\\actriz.png')

nueva = np.zeros((mascara.shape), dtype= 'uint8')

nueva[:] = (0, 128, 255)

for i in range(len(mascara)):
    for j in range(len(mascara[0])):
        if (mascara[i, j] != (255, 255, 255)).all():
            nueva[i, j] = imagen[i, j]

cv.imshow('actriz.png', nueva)

cv.waitKey(0)

cv.destroyAllWindows()