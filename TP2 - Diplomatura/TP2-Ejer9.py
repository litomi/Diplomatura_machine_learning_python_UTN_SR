# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 01:07:22 2022

@author: Lisandro
"""

# =============================================================================
# 9. Crear un vector con un total de 50 elementos equidistantes
#  en el intervalo [1, 6].
# =============================================================================

#artesanal
#([a, b], cantidad de partes) -> lista
def equidistantes(a, b, partes):
    dif = (-(b - a) if (b - a) < 0 else  (b - a))/ (partes - 1)    
    puntos = [a]    
    for i in range(1, partes):
        puntos.append(puntos[i - 1] + dif)        
    return puntos

#numpy
import numpy as np
r = np.linspace(1, 6, 50)
