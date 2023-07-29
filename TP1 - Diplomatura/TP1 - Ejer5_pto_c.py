# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:48:10 2022

@author: Lisandro
"""

# =============================================================================
# 5.Grafique
#     
# c) 
#     f1(x) = cos(x)
#     f2(x) = sin(x) en [-3, 3]
# 
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

x = [n/100 for n in range(-314, 315)]

fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(8)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.grid()
plt.xlabel("X")
plt.xticks([-3.14, -1.57, 0, 1.57, 3.14], 
           ["-$\pi$", "$-\pi/2$", "0", "$\pi/2$", "$\pi$"])
plt.legend(["$sen(x)$", "$cos(x)$"])
plt.show()