import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

#-----------------------------------------------------
# Devuelve imagen en dos colores, negro y blanco.
# Imagen: gris en 1 canal
# umbral
#-----------------------------------------------------
def bn(imagen, umbral):
    copia = imagen.copy()
    for i in range(len(copia)):
        for j in range(len(copia[0])):
            copia[i, j] = 255 if copia[i, j] > umbral else 0
    return copia

#-----------------------------------------------------
def binaria_invertida(imagen, umbral):
    copia = imagen.copy()
    for i in range(len(copia)):
        for j in range(len(copia[0])):
            copia[i, j] = 255 if copia[i, j] <umbral else 0
    return copia

#-----------------------------------------------------
# Devuelve imagen en dos colores, negro y gris.
# imagen en grises en 3 canales
# umbral
#-----------------------------------------------------
def bn_gris_3_canales(imagen, umbral):
    copia = imagen.copy()
    for i in range(len(copia)):
        for j in range(len(copia[0])):
            for k in range(len(copia[0, 0])):
                copia[i, j][k] = 180 if copia[i, j][k] > umbral else 0
    return copia

#-----------------------------------------------------
# Devuelve matriz de datos con los valores 
# de cada pixel. [0 - 255]
# imagen_gris
#-----------------------------------------------------
def histograma_datos(imagen_gris):
    valores = np.array([0 for i in range(256)])
    for i in imagen_gris.flat:
        valores[i] += 1
    return valores

#-----------------------------------------------------
# Devuelve matriz con la cantidad de pixeles por valor
# entre 0 y 255
# Imagen: 3 canales
# canal: canal del cual obtener valores
#-----------------------------------------------------

def valoresPixeles(imagen, canal):
    valores = np.array([0 for i in range(256)])    
    for i in range(len(imagen)):
        for j in range(len(imagen[0])):
            valores[imagen[i, j][canal]] += 1
    return valores

#-----------------------------------------------------
# Genera el histograma de un canal de una imagen
# imagen
# canal: canal sobre el que se hará el histograma
# Blue: 0, Green: 1, Red: 2
#-----------------------------------------------------
def histograma(imagen, canal):
    try:
        plt.plot(valoresPixeles(imagen, canal), color= 'black')
        plt.show()
    except:
        print("ERROR: no hay imagen.")


########################################################################

#-----------------------------------------------------
# Devuelve una imagen en grises con 3 valores por pixel.
# imagen
#-----------------------------------------------------
def luma_tres_valores(imagen):
    copia = imagen.copy()
    for i in range(len(copia)):
        for j in range(len(copia[i])):
            a, b, c = copia[i][j]
            gris = (c * 0.2126) + (b * 0.7152) + (a * 0.0722)
            for h in range(len(copia[i][j])):
                copia[i][j][h] = gris
    return copia

#-----------------------------------------------------
# Devuelve una imagen en grises con 1 valor por pixel.
# imagen
#-----------------------------------------------------
def luma(imagen):
    nueva = np.zeros((imagen.shape[0], imagen.shape[1]), dtype='uint8')
    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            a, b, c = imagen[i][j]
            gris = (c * 0.2126) + (b * 0.7152) + (a * 0.0722)
            nueva[i, j] = gris
    return nueva

#-----------------------------------------------------
# Devuelve una imagen en grises con 1 valor por pixel.
# imagen
#-----------------------------------------------------
def promedio(imagen):
    nueva = np.zeros((imagen.shape[0], imagen.shape[1]), dtype='uint8')
    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            gris = (sum(imagen[i][j]) / len(imagen[i][j]))
            gris = 255 if gris > 255 else gris
            nueva[i][j] = gris
    return nueva


#-----------------------------------------------------
# Devuelve una imagen en grises con 1 valor por pixel.
# imagen
#-----------------------------------------------------
def desaturar(imagen):
    copia = np.zeros((imagen.shape[0], imagen.shape[1]), dtype='uint8')
    for i in range(len(copia)):
        for j in range(len(copia[i])):
            gris = (max(imagen[i][j]) + min(imagen[i][j]) / 2)
            gris = 255 if gris > 255 else gris
            copia[i, j] = gris
    return copia


###########################################################################################
#-----------------------------------------------------
# imagen
# patrón : normalizado
#-----------------------------------------------------
def convolucionar(imagen, patron):
    nueva = np.zeros((imagen.shape), dtype='float')

    margen = int(len(patron[0]) / 2)

    for i in range(margen, len(imagen) - margen):
        for j in range(margen, len(imagen[0]) - margen):
            aux = 0            
            for k in range(-margen, len(patron) - margen):
                for l in range(-margen, len(patron[0]) - margen): 
                    aux += (imagen[i - k, j - l] * patron[l + margen, k + margen])
                    
            if aux > 255:
                aux = 255
            elif aux < 0:
                aux = 0

            nueva[i, j] = aux

    return nueva.astype('uint8')
    
#################################################################################
#-----------------------------------------------------
# Refleja la imagen respecto a un eje
# imagen
# orientación = ['horizontal] ['vertical]# 
#-----------------------------------------------------

def flip(imagen, eje = "horizontal"):
    if eje != 'horizontal' and eje != 'vertical':
        return None

    nueva = np.zeros(imagen.shape, dtype='uint8')

    for i in range(len(imagen)):
        for j in range(len(imagen[0])):
            if eje == 'vertical':
                nueva[i, j] = imagen[i, len(imagen[0]) - 1 - j]
            elif eje == 'horizontal':
                nueva[i, j] = imagen[len(imagen) - 1 - i, j]

    return nueva

#-----------------------------------------------------
# Rota una imagen
# imagen
# grados = [90][180][270] 
#-----------------------------------------------------
def rotar(imagen, grados):
    if grados == 90 or grados == 270:
        orientacion = (imagen.shape[1], imagen.shape[0], 3)
    elif grados == 180:
        orientacion = imagen.shape
    else:
        return None
    
    nueva = np.zeros( orientacion, dtype='uint8')

    for i in range(len(imagen)):
        for j in range(len(imagen[0])):
            if grados == 90:
                nueva[len(nueva) - 1 - j, i] = imagen[i, j]
            elif grados == 180:
                nueva[len(nueva) - 1 - i, len(nueva[0]) - 1 - j] = imagen[i, j]
            else:
                nueva[j, len(nueva[0]) - 1 - i] = imagen[i, j]

    return nueva