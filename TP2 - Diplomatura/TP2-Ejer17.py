# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 05:08:46 2022

@author: Lisandro
"""

# =============================================================================
# 17. Implemente una función que tome un escalar y una matriz y devuelva
# la matriz resultante de multiplicar ese escalar por ella misma.
# =============================================================================


#artesanal
#suponiendo dos dimensiones
def matriz_por_escalar(matriz, escalar):
    for f in matriz:
        for c in range(len(f)):
            f[c] *= escalar
    return matriz

#numpy
import numpy as np
def matriz_por_escalar_numpy(matriz, escalar):
    return np.multiply(matriz, escalar)

