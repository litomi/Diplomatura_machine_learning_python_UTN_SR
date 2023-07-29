import numpy as np
from Personal.funciones import *

xs = np.array([4.1, 6, 6, 7.3, 7.8, 8.1, 8.77,
              9.45, 12.3, 14.2, 15, 16, 18.12])
ys = np.array([90, 89, 83, 81, 73, 71, 68, 60, 59, 54, 35, 35, 21])


if __name__ == "__main__":
    #optimización
    paso = 0.001
    tolerancia = 0.001

    #Calcular
    m, b, costo = calcular_recta(xs, ys, paso, tolerancia)

    #Consola
    print("Pendiente: %2.2f" % m)
    print("Ordenada al origen: %2.2f" % b)

    #Grafica
    graficar(xs, ys, m, b)