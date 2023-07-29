# 1. Diseñar una función que genere el histograma de una imagen en escala de grises, que
# se le dé como argumento. Graficar el histograma de alguna imagen cualquiera, que haya
# convertido previamente a escala de grises, utilizando la librería matplotlib. Puede optar
# por implementarla como un procedimiento que directamente realice la gráfica del mismo,
# al ser llamada. O podría ser una función cuyo retorno sea el histograma, y luego en el
# programa principal realizar la gráfica. Lo que crea más conveniente para su uso actual.
# Notar que en este caso, estaremos haciendo la versión más simple de histograma, que es
# efectivamente la frecuencia de todos los valores. (No se hará una agrupación por rangos
# de valores o bins)

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from Personal.funciones import *

#-------------------------------------------------
imagen = cv.imread('imagenes\\actor.png')
valores = histograma_datos(luma(imagen))
plt.plot(valores, color='gray' )
plt.title("Histograma")
plt.xlabel("Valores de pixel")
plt.ylabel("Cantidad de pixeles")
plt.show()