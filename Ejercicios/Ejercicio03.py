#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:31:05 2017

@author: danielmorales
"""

# Leer 2 numeros y que nos diga si son iguales o cual es mayor

n1 = int(input("Ingresa el primer valor "))

n2 = int(input("Ingresa el segundo valor -7"))

if n1 == n2:
    print(n1," y ",n2," son iguales")
    
elif n1 > n2:
    print(n1," es mayor a ",n2)
    
elif n1 < n2:
    print(n2," es mayor a ",n1)

else:
    print("Error")
