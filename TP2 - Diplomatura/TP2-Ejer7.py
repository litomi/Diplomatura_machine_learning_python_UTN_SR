# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:21:45 2022

@author: Lisandro
"""

# =============================================================================
# 7.Crear un vector de 10 números cualesquiera, con el método que más
# le guste. Invertir su orden. Desarrollar dos versiones del código, 
# artesanal sin métodos de Numpy y sofisticado utilizando las
# características que nos provee Numpy.
# =============================================================================
import random as ran
import numpy as np
vector = [ran.randint(-100, 100) for i in range(10)]


#Artesanal
aux = []
for i in range(len(vector) - 1, -1, -1):
    aux.append(vector[i])
vector = aux

#Numpy
vector = np.array(vector)
np.flip(vector)