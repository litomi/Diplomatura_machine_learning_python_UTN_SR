# 5. Dada la imagen llamada ciudad.jpg utilice el histograma, para analizar cual sería un buen
# valor de umbral para separar los edificios del cielo.

import cv2 as cv
from Personal.funciones import *

imagen = cv.imread('imagenes\\ciudad.jpg')
imagen = luma(imagen)
valores = histograma_datos(imagen)

#histograma
plt.plot(valores )
plt.title("Histograma - ciudad.jpg")
plt.grid()
plt.savefig('imagenes\\histograma_ciudad.jpg')
plt.show()

#Viendo el histograma, aproximadamente es un umbral de 185
imagen = bn(imagen, 185)
cv.imshow('imagen', imagen)
cv.waitKey(0)