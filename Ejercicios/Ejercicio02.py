#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 00:57:35 2017

@author: danielmorales
"""

# Pedir 3 números, si el primero es negativo, devolver producto de los 3, sino, la suma

n1 = int(input("Ingresa el primer numero: "))

n2 = int(input("Ingresa el segundo numero: "))

n3 = int(input("Ingresa el tercer numero: "))

if n1<0:
    resultado = n1*n2*n3
    print("Como el primer valor es negativo, la multiplicacion de los valores es: ",resultado)
    
else:
    resultado = n1+n2+n3
    print("Como el primer valor es positivo, la suma de los valores es: ",resultado)
