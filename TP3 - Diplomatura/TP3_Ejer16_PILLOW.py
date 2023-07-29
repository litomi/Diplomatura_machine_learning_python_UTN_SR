# 16. Convertir una imagen a escala de grises, de modo artesanal. Dejarla implementada como
# una función propia que dado un nombre de archivo de imagen devuelva o la imagen lista,
# o grabe la imagen a disco, segóun un paróametro extra de la función, llamado retorno que
# tome uno de dos valores posibles ('disco', 'imagen').
# Realice diferentes implementaciones:
# a)Promedio.
# b)Corrección para el Ojo humano (Luma por ejemplo).
# c)Descomposición/Desaturación por máxima y mínima.
# d)Un óunico canal.

import cv2 as cv
import numpy as np
from PIL import Image as mg 

def promedio(url_imagen, retorno  = 'disco'):
    try:
        imagen = mg.open(url_imagen)
        matriz = np.array(imagen)

        for i in range(imagen.height):
            for j in range(imagen.width):
                lista = (imagen.getpixel((j, i)))
                gris = (sum(lista)) / len(lista)
                for h in range(len(matriz[i][j])):
                    matriz[i][j][h] = gris

        if retorno == 'disco':
            mg.save('imagenes\{}_promedio'.format(url_imagen), mg.fromarray(matriz))
        
        if retorno == 'imagen':
            return mg.fromarray(matriz)

    except:
        return None

def luma(url_imagen, retorno  = 'disco'):
    try:
        imagen = mg.open(url_imagen)
        matriz = np.array(imagen)

        for i in range(imagen.height):
            for j in range(imagen.width):
                r, g, b = imagen.getpixel((j, i))
                gris = (r * 0.2126) + (g * 0.7152) + (b * 0.0722)
                for h in range(len(matriz[i][j])):
                    matriz[i][j][h] = gris

        if retorno == 'disco':
            mg.save('imagenes\{}_luma'.format(url_imagen), mg.fromarray(matriz))
        
        if retorno == 'imagen':
            return mg.fromarray(matriz)

    except:
        return None

def desaturar(url_imagen, retorno  = 'disco'):
    try:
        imagen = mg.open(url_imagen)
        matriz = np.array(imagen)
        
        for i in range(imagen.height):
            for j in range(imagen.width):
                lista = imagen.getpixel((j, i))
                gris = (max(lista) + min(lista)) / 2
                for h in range(len(matriz[i][j])):
                    matriz[i][j][h] = gris

        if retorno == 'disco':
            mg.save('imagenes\{}_desaturar'.format(url_imagen), mg.fromarray(matriz))
        
        if retorno == 'imagen':
            return mg.fromarray(matriz)

    except:
        return None










