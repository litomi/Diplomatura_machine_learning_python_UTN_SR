# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:38:00 2022

@author: Lisandro
"""

# =============================================================================
# 14.Implemente una función prom_ponderado que tome dos listas de valores,
# una con los datos y la otra con los pesos, y devuelva el promedio ponderado.
# =============================================================================
def prom_ponderado(datos, pesos):
    suma = 0
    ponderaciones = 0
    
    if(len(datos) != len(pesos)):
        return -1
    
    for i in range(len(datos)):
        ponderaciones += pesos[i]
        suma += datos[i] * pesos[i]
        
    return suma / ponderaciones
