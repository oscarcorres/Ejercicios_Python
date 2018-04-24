#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Ejercicios de la Unidad 04: Programación Orientada a Objetos
#
# Perpetrados por: Oscar Corres y Viloria

# 4-  Crear una función crea_listado que sea capaz de crear un listado de n elementos y devolverlo.
#     N será un parámetro que pasarás a la función, será 0 por defecto. Que recibirá otro parámetroç
#     que deberá indicar el valor inicial de cada elemento del listado, que será 0 por defecto.
#     Esta función deberá estar presente en el módulo.

def creaListado(numElementos=0, elemento=0):
    return [eval(str(elemento)) for x in range(numElementos)]