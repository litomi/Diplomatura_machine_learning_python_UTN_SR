# 11. Implementar 3 funciones, cada una se encargará de eliminar uno de los tonos de una imagen
# cualquiera. Las funciones llamadas quitar rojo, quitar azul y quitar verde tomarán
# un solo parámetro, la imagen.

import cv2 as cv

def quitar_rojo(imagen):
    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            imagen[i][j][2] = 0 

def quitar_verde(imagen):
    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            imagen[i][j][1] = 0 


def quitar_azul(imagen):
    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            imagen[i][j][0] = 0 
