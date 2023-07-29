# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 02:46:05 2022

@author: Lisandro
"""

# =============================================================================
# 12. Generar la siguiente matriz e imprimirla en pantalla. Realizar dos 
# versiones de código, una artesanal y otra versión utilizando rebanadas:
# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1
# =============================================================================
import numpy as np
#Artesanal
matriz = np.array([[0 if f % 2 != 0 else 1 for c in range(5)] for f in range(5)])

#Rebanadas
matriz = np.zeros((5, 5))
matriz[::2] = 1