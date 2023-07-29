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

def promedio(url_imagen, retorno = 'disco'):

    imagen = cv.imread(url_imagen, 1)

    if imagen is None:
        return None

    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            gris = (sum(imagen[i][j]) / len(imagen[i][j]))
            gris = 255 if gris > 255 else gris
            for h in range(len(imagen[i][j])):
                imagen[i][j][h] = gris

    if retorno == 'imagen':
        return imagen
    
    if retorno == 'disco':
        cv.imwrite('imagenes\imagen-ejer15.jpg', imagen)

def luma(url_imagen, retorno = 'disco'):

    imagen = cv.imread(url_imagen, 1)

    if imagen is None:
        return None

    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            a, b, c = imagen[i][j]
            gris = (c * 0.2126) + (b * 0.7152) + (a * 0.0722)
            for h in range(len(imagen[i][j])):
                imagen[i][j][h] = gris

    if retorno == 'imagen':
        return imagen
    
    if retorno == 'disco':
        cv.imwrite('imagenes\imagen-ejer15.jpg', imagen)

def desaturar(url_imagen, retorno = 'disco'):

    imagen = cv.imread(url_imagen, 1)

    if imagen is None:
        return None

    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            gris = (max(imagen[i][j]) + min(imagen[i][j]) / 2)
            gris = 255 if gris > 255 else gris
            for h in range(len(imagen[i][j])):
                imagen[i][j][h] = gris

    if retorno == 'imagen':
        return imagen
    
    if retorno == 'disco':
        cv.imwrite('imagenes\imagen-ejer15.jpg', imagen)


