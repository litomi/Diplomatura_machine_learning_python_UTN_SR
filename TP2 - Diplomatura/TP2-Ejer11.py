# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 02:34:14 2022

@author: Lisandro
"""

# =============================================================================
# 11. Crear un array de 20 filas por 8 columnas. Llenarlo con valores al azar.
# Mostrar en pantalla. Luego, calcular la suma de todos sus valores.
# =============================================================================


#artesanal
import random as ran
matriz = [[ran.randint(-1000, 1000) for i in range(8)] for j in range(20)]
total = 0
for i in matriz:
    for j in i:
        print(("%5d") % (j), end = "")
        total += j
    print(" ")
print("Total: ", total)

#numpy
import numpy as np
matriz = np.random.randint(-1000, 1000, size = (20, 8))
print(matriz)
print("Suma: ", np.sum(matriz))