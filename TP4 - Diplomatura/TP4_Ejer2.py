# 2. Diseñar una función que genere el histograma de un solo color, el que se elija, dada una
# imagen color pasada como argumento.

import cv2 as cv
import numpy as np
from Personal.funciones import histograma

imagen = cv.imread('imagenes\\spider.jpeg')

histograma(imagen, 0)
histograma(imagen, 1)
histograma(imagen, 2)