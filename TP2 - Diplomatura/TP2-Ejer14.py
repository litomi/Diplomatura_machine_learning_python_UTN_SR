# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 03:41:39 2022

@author: Lisandro
"""

# =============================================================================
# 14. Determinar la cantidad de butacas libres en una sala de cine. 
# Para representar la sala de butacas, suponga un array con valores
# booleanos que si es verdadero indica que esa butaca está ocupada 
# y si es falso, la butaca está desocupada.
# =============================================================================

import random as ran
import numpy as np

#artesanal
sala = np.array([[ran.choice([True, False]) for f in range(10)] for c in range(10)])
libres = 0
for i in sala:
    for j in range(len(i)):
        if i[j] == False:
            libres += 1
            
#numpy
sala = np.random.choice([True, False], size = (10, 10))
libres = sala[sala == False].size
