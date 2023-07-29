# 6. Dada la imagen llamada actriz.png genere una versión binaria de la misma. Refine su
# versión analizando el histograma de la misma.

import cv2 as cv
from Personal.funciones import *

imagen = cv.imread('imagenes\\actriz.png')
imagen = promedio(imagen)

#histograma
valores = histograma_datos(imagen)
plt.plot(valores )
plt.title("Histograma - actriz.png")
plt.grid()
plt.savefig('imagenes\\histograma_actriz.png')
plt.show()


imagen = bn(imagen, 163)
cv.imshow('actriz_bicolor.png', imagen)
cv.waitKey(0)
cv.imwrite('imagenes\\actriz_bicolor.png', imagen)
