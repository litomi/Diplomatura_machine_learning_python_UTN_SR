import numpy as np
from Personal.funciones import calcular_recta, graficar

if __name__ == "__main__":
    # Datos
    xs = np.array([2, 3, 4, 5, 6, 7])
    ys = np.array([18, 33, 37, 54, 59, 71])

    # Parámetros de optimización
    paso = 0.01
    tolerancia = 0.000000001

    # Calcular
    m, b, costo = calcular_recta(xs, ys, paso, tolerancia)

    # Graficar
    graficar(xs, ys, m, b)

    print("Pendiente (m):", m)
    print("Ordenada al origen (b):", b)
    print("Costo:", costo)
