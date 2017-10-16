#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:51:35 2017

@author: danielmorales
"""

#Leer 3 numeros distintos y nos diga cual es el mayor

n1 = int(input("Ingresa el primer numero "))
n2 = int(input("Ingresa el segundo numero "))
n3 = int(input("Ingresa el tercer numero "))

if n1>n2 and n1>n3:
    print(n1," es mayor a ",n2," y ",n3)
    
elif n2>n1 and n2>n3:
    print(n2," es mayor a ",n1," y ",n3)
    
elif n3>n1 and n3>n2:
    print(n3," es mayor a ",n1," y ",n2)

else:
    print("Otro resultado")
