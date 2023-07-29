# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:59:18 2022

@author: Lisandro
"""

# =============================================================================
# 8.Implemente la función signo y grafiquela en el intervalo [-4, 4]. 
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(-4, 0, .1)
x2 = 0
x3 = np.arange(np.diff(x1)[0], 4, .1)

plt.plot(x1, np.sign(x1), "g")
plt.plot(x2, np.sign(x2), "go")
plt.plot(x3, np.sign(x3), "g")
plt.show()