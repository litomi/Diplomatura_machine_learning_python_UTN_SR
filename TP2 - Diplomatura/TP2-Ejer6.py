# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:15:55 2022

@author: Lisandro
"""

# =============================================================================
# 6.Crear un vector con números enteros al azar entre 0 y 6.
# Luego reemplazar los 0 con 6.
# =============================================================================
import numpy as np

vector = np.random.randint(6, size = 100)

vector[vector == 0] = 6