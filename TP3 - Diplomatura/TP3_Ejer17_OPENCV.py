
# Implementar una funcióon que genere una versión en tonos sepia de una imagen pasada
# como argumento. Una posibilidad es utilizar los valores recomendados por Microsoft para
# generar un pixel sepia en base a un pixel RGB, dado por los siguientes valores.
# el nuevo rojo pasaróa a ser (R * .393) + (G * .769) + (B * .189)
# el nuevo verde seróa (R * .349) + (G * .686) + (B * .168)
# y el nuevo azul seróa (R * .272) + (G * .534) + (B * .131)

import cv2 as cv

def sepia(imagen):
    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            B, G, R = imagen[i, j]
            b2 = (R * .272) + (G * .534) + (B * .131) #azul
            b2 = 255 if b2 > 255 else b2

            g2 = (R * .393) + (G * .769) + (B * .189) #rojo
            g2 = 255 if g2 > 255 else g2

            r2 = (R * .349) + (G * .686) + (B * .168) #verde
            r2 = 255 if r2 > 255 else r2

            imagen[i, j] = (b2, g2, r2)
            
    return imagen

    
img = cv.imread('imagenes\\ejer3.jpg')

cv.imshow('', img)

cv.waitKey(0)

imagen = sepia(img)

cv.imshow('', imagen)

cv.waitKey(0)

cv.destroyAllWindows()