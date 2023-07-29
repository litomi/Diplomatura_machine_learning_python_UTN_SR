# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:56:09 2022

@author: Lisandro
"""

# =============================================================================
# 7. Grafique la función erf() en el intervalo [-4; 4]. (Tip: Puede utilizar la 
# función ya definida erf() de la librería math; erf es la función error)
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-4, 4)
y = [math.erf(x) for x in x]

fig = plt.figure() 
fig.set_size_inches(10, 5)

plt.plot(x, y)
plt.legend(["erf()"])
plt.show()