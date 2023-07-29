# 17. Implementar una función que genere una versión en tonos sepia de una imagen pasada
# como argumento. Una posibilidad es utilizar los valores recomendados por Microsoft para
# generar un pixel sepia en base a un pixel RGB, dado por los siguientes valores.
# el nuevo rojo pasará a ser (R * .393) + (G * .769) + (B * .189)
# el nuevo verde será (R * .349) + (G * .686) + (B * .168)
# y el nuevo azul será (R * .272) + (G * .534) + (B * .131)
import cv2 as cv

def sepia(imagen):
    for i in range(len(imagen)):
        for j in range(len(imagen[i])):
            azul, verde, rojo = (imagen[i][j])
            azul = (rojo * .272) + (verde * .534) + (azul * .131)
            verde = (rojo * .349) + (verde * .686) + (azul * .168)
            rojo = (rojo * .393) + (verde * .769) + (azul * .189)
            imagen[i][j] = azul, verde, rojo
