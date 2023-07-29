# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 03:28:22 2022

@author: Lisandro
"""

# =============================================================================
# 13. Generar la siguiente matriz cuadrada, es decir, misma cantidad de 
# las que de columnas, e imprimirla en pantalla, en dos versiones de código,
# una utilizando bucles y un código artesanal, sin comandos de Numpy,
# solo el array y las posiciones. Y otra versión, utilizando todas las 
# ventajas de disponer de Numpy (ídem para los ejercicios de este estilo
# posteriores):
# 1 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 1 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 1 0
# 0 0 0 0 0 1
# =============================================================================

#artesanal
matriz = [ [1 if f == c else 0 for f in range(6)] for c in range(6)]
print(matriz)

#numpy
import numpy as np
matriz = np.zeros((6, 6))
np.fill_diagonal(matriz, 1)
