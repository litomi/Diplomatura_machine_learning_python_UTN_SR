# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:36:00 2022

@author: Lisandro
"""

# =============================================================================
# 4.Resuelva este ejercicio de dos modos: primero realice las cuentas en papel,
# luego implemente la función en Python. Determinar si las siguientes dos
# rectas se cruzan en un punto o no. En papel, determinar en qué punto en 
# concreto se cruzan, si es que lo hacen.
# a)  f(x) = 2x + 1
#     f(x) = 6 - 3x
# b)  f(x) = 2x + 1
#     f(x) = 2x - 3
# c)  f(x) = 1 - 2x
#     f(x) = 3x + 6
# =============================================================================
class Recta:
    m = 0
    b = 0
    
    def __init__(self, m, b):
        self.m = m
        self.b = b
    
    def __str__(self):
        return (
            ("%dx%c%d") % (self.m, "+" if self.b > 0 else " ", self.b)
            )
        
def intersectan(r1, r2):
    return (r1.m != r2.m)

def pto_inter(r1, r2):
    x = ((r2.b - r1.b) / (r1.m - r2.m))
    return (x, (r1.m * x + r1.b))

r1 = Recta(2, 1)
r2 = Recta(-3, 6)
print( "a)", r1, "y" ,r2, "se intersectan." if intersectan(r1, r2)
      else "no se intersectan.")

r1 = Recta(2, 1)
r2 = Recta(2, -3)
print( "b)", r1, "y" ,r2, "se intersectan." if intersectan(r1, r2)
      else "no se intersectan.")

r1 = Recta(-2, 1)
r2 = Recta(3, 6)
print( "c)", r1, "y" ,r2, "se intersectan." if intersectan(r1, r2)
      else "no se intersectan.")