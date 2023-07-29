# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:32:16 2022

@author: Lisandro
"""

# =============================================================================
# 8. Crear una matriz de 6 x 6, con valores que van de 1 a 9. 
# Mostrar en pantalla los elementos que pertenecen a la diagonal de la matriz.
# ============================================================================
import numpy as np

matriz = np.random.randint(1, 10, size = (6, 6))


#artesanal
for i in range(len(matriz)):
    print(matriz[i][i], end=" ")

#numpy
print(np.diagonal(matriz))
