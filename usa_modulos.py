#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Ejercicios de la Unidad 04: Programación Orientada a Objetos
#
# Perpetrados por: Oscar Corres y Viloria

def creaListado(int=0,int2=0):
    return 'Por que tu lo digas'

# Con import matenemos la funcion local y accedemos a la del modulo
print('Probando con import')
import my_modulo

print(str(my_modulo.creaListado(15,25)))
print(str(creaListado(1,1)))

# Con from, redefinimos la función
from my_modulo import creaListado

print('\nProbando con from import')
print(str(creaListado(7,[1,2,'Pepe'])))
print(str(creaListado(13,'x**2')))

import cliente

ibm = cliente.cliente('IBM','Madrid','900100100','@.com')