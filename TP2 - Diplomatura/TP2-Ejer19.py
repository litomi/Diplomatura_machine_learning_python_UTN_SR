# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:37:07 2022

@author: Lisandro
"""

# =============================================================================
# 19.Implemente una función que tome dos matrices de dos dimensiones cada una, 
# y devuelva la matriz resultante de multiplicar ambas. ¿Qué debe controlar 
# para poder realizar el producto entre ambas?
# Respuesta: Se debe controlar que la cantidad de columnas de la primera 
# matriz sea igual a la cantidad de filas de la segunda.
# =============================================================================

#artesanal
def multiplica_matrices(m1, m2):
    if len(m1[0]) == len(m2): #columnas m1 == filas m2    
        m3 = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]    
        for i in range(len(m1)): #filas m1
            for j in range(len(m2[0])): #columnas m2
                for k in range(len(m2)):
                    m3[i][j] += m1[i][k] * m2[k][j]
        return m3
    return

#numpy
import numpy as np
def multiplica_matrices_numpy(m1, m2):
    return np.dot(m1, m2)
