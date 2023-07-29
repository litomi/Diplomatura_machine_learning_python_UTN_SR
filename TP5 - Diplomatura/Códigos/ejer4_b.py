import numpy as np
from Personal.funciones import *

xs = np.array([4.1, 6, 6, 7.3, 7.8, 8.1, 8.77,
              9.45, 12.3, 14.2, 15, 16, 18.12])
ys = np.array([90, 89, 83, 81, 73, 71, 68, 60, 59, 54, 35, 35, 21])


if __name__ == "__main__":
    # rangos
    rango_m = np.arange(-10, 0, 0.1)
    rango_b = np.arange(100, 201)

    # Partidas
    costo_optimo = float('inf')  # Asigna un valor muy grande
    m_optimo = 0
    b_optimo = 0

    for m in rango_m:
        for b in rango_b:
            costo = calcular_costo(xs, ys, m, b)
            if costo < costo_optimo:
                costo_optimo = costo
                m_optimo = m
                b_optimo = b

    # Resultados
    print("Pendiente: %2.2f" % m_optimo)
    print("Ordenada al origen: %2.2f" % b_optimo)

    # Graficar
    graficar(xs, ys, m_optimo, b_optimo)
