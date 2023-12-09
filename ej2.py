"""
Programa que calcula el área y el perímetro de un círculo.
Autor: CZ
Fecha: 20 octubre de 2023
"""

#Cree un programa que tome el radio de un círculo e imprima su área y perímetro.

import math

r = float(input("Ingrese el radio del círculo: "))

print("El área del círculo es: {:.2f}".format(math.pi * r ** 2))
print("El perímetro del círculo es: {:.2f}".format(2 * math.pi * r))
