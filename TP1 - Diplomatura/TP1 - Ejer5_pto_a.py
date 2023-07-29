# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:43:45 2022

@author: Lisandro
"""

# =============================================================================
# 5.Grafique
# 
# a) 
#     f(x) = 3x^2 en [-2, 2]
# 
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np

# a)
x = np.arange(-2, 2, 0.01)
f = [3*x**2 for x in x]

fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(8)

plt.plot(x, f)
plt.grid()
plt.legend(["f(x) = $3x^{2}$"])
plt.show()