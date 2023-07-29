# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 04:36:25 2022

@author: Lisandro
"""

# =============================================================================
# 16.Implemente una función que tome como parámetros dos matrices y 
# devuelva la suma de ambas. Realice una versión artesanal sin utilizar
# el + de Numpy. Es importante que desarrolle soltura para hacer operaciones 
# con elementos de matrices, elemento a elemento, maneje los índices, etc.
# =============================================================================

#artesanal
def suma_matrices(m1, m2):     
    if m1.size == m2.size:        
        m3 = np.zeros([len(m1), len(m1[0])]) 
        for f in range(len(m1)):
            for c in range(len(m1[f])):
                m3[f][c] = m1[f][c] + m2[f][c]                
        return m3
    return

#numpy
import numpy as np
def suma_matrices_numpy(m1, m2):
    return np.add(m1, m2)
