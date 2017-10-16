#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 00:36:27 2017

@author: danielmorales
"""
#Ejercicio 01
#Ingresar una nota del 1 al 7, si es de 4 hacia arriba mostrar un mensaje de aprobado y en caso contrario mostrar un desaprobado

while nota != 0:

    nota = int(input("Ingresa tu nota y te dire si aprobaste o no: "))
  
    if nota < 1 or nota > 7:
        print("Nota ingresada esta fuera del rango")
        
    elif nota >= 4 and nota <= 7:
        print("Has aprobado")
        
    else:
        print("Has reprobado")
