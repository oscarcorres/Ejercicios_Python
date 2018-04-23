#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Ejercicios de la Unidad 04: Programación Orientada a Objetos
#
# Perpetrados por: Oscar Corres y Viloria

class cliente:
    def __init__(self, nombre, direccion, tlf, email):
        self.nombre = nombre
        self.direccion = direccion
        self.tlf = tlf
        self.email = email