# 7. Crear una imagen de tamañoo cuadrado desde cero, donde el usuario ingrese el color de
# fondo que desea, y el color para el cuadrado que se dibujará en el centro. Generar una
# imagen que contenga un pequeño cuadrado en el centro de la misma.

import cv2 as cv
import numpy as np

colores = (
    (0, 0, 0), #negro
    (255, 255, 255), #blanco
    (255, 0, 0), #azul
    (0, 255, 0), #verde
    (0, 0, 255), #rojo
    (255, 255, 0), #cyan
    (0, 255, 255), #amarillo
    (255, 0, 255) #magenta
)

def menu():
    print("Colores:")
    print("1.- negro ")
    print("2.- blanco ")
    print("3.- azul ")
    print("4.- verde ")
    print("5.- rojo ")
    print("6.- cyan ")
    print("7.- marillo ")
    print("8.- magenta ")

def ingreso():
    n = 0
    while True:
        try:
            n = int(input("-> "))
            if n < 1 or n > 8:
                raise exception()
            break;
        except:
            print("Sólo números del menú.")
    return n

def dibujar(fondo, fondo_centro):
    marco = np.zeros((500, 500, 3), dtype='uint8')
    marco[:] = colores[fondo - 1]
    inicio = (int(len(marco) / 3), int(len(marco[0]) / 3))
    fin = (int(len(marco) / 3) * 2, int(len(marco[0]) / 3) * 2)
    imagen = cv.rectangle(marco, inicio, fin, colores[fondo_centro - 1], -1)
    return imagen

#ejecución1
menu()
print("Ingrese un color para el fondo: ")
fondo = ingreso()
print("Ingrese un color para el cuadradro central: ")
fondo_centro = ingreso()

img = dibujar(fondo, fondo_centro)

cv.imwrite('imagenes/tp3-ejer7-cuadrados-centro.jpg', img)

cv.imshow('', img)

cv.waitKey(0)

cv.destroyAllWindows()