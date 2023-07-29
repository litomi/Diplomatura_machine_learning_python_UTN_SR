# 9. Pedir una imagen al usuario y generar una nueva imagen que agregue un padding de 50px
# todo alrededor, del color que el usuario desee. Luego, generalizar en una función llamada
# padding que tome como parámetros una imagen y un valor de pixeles, y genere una nueva
# imagen que conste de la original más un borde de dicho grosor de pixeles todo alrededor.

import cv2 as cv
import numpy as np

#---------------------------------------------
#colores
colores = (
    (255, 255, 255), #blanco
    (0, 0, 0), #negro
    (255, 0, 0), #azul
    (0, 0, 255), #rojo
    (0, 255, 255), #amarillo
    (0, 128, 0), #verde
    (165, 0,255), #naranja
    (130, 0, 75) #índigo
)

# -------------------------------------------
# url_imagen = dirección y nombre de la imagen
# borde = ancho en pixeles del borde
# color = color del borde como tupla

def padding_simple(imagen, borde, color):

    imagen = cv.imread(imagen, 1)

    if imagen is None:
        return None

    alto, ancho, canales = imagen.shape
    marco = np.zeros((alto + (borde*2), ancho + + (borde*2), 3), dtype='uint8')
    marco[:] = color

    for i in range(alto):
        for j in range(ancho):
            marco[borde + i, borde + j] = imagen[i, j]

    return marco

#-----------------------------------------------------
#
def menu_colores():
    print("Colores: ");
    print("1.- blanco")
    print("2.- negro")
    print("3.- azul")
    print("4.- rojo")
    print("5.- amarillo")
    print("6.- verde")
    print("7.- naranja")
    print("8.- índigo")

#------------------------------------------------------
#
def ingreso(min, max):
    while True:
        try:
            n = int(input(": "))
            if n < min or n > max:
                raise exception
            return n
        except:
            print("Sólo número entre {} y {}".format(min, max))


#  ------------APLICACIÓN---------------------------------------------
camino = "imagenes\\" + input("Ingrese nombre de la imagen (*.ext): ")

print("Seleccionar un color:")
menu_colores()
color = ingreso(1, 8)

print("Ingrese tamaño del borde en pixwles:")
pixeles = ingreso(0, 100)

img = padding_simple(camino, pixeles, colores[color - 1])

if img is not None:    
    cv.imshow('', img)
    cv.waitKey(0)
else:
    print("No se pudo abrir la imagen.")
    
