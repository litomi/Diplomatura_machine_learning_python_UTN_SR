# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 02:21:28 2022

@author: Lisandro
"""

# =============================================================================
# 10. Crear una matriz de 200 x 100 con números al azar, elegir un tipo 
# de dato diferente al float por defecto.
# =============================================================================

import numpy as np

matriz = np.random.randint(-100, 100, size = (200, 100), dtype = "int16")