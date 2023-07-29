# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 04:07:26 2022

@author: Lisandro
"""

# =============================================================================
# 15. Dada una matriz de 20 filas por 30 columnas, con valores enteros al azar,
# generar una matriz llamada es_par que tendrá valores booleanos,
# verdadero si el número en la matriz original es par o falso sino.
# =============================================================================

#artesanal
import random as ran
enteros = [[ ran.randint(0, 100) for c in range(30)] for f in range(20)]
es_par = [[True for c in range(30)] for f in range(20)]

for f in range(len(enteros)):
    for c in range(len(enteros[f])):
        if enteros[f][c] % 2 != 0:
            es_par[f][c] = False
        
#numpy
import numpy as np
enteros = np.random.randint(0, 100, size = (30, 20))
es_par = enteros % 2 == 0
