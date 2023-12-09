"""
Programa que calcula el porcentaje x sobre una cantidad x.
Autor: Christian Zambrano
Fecha: Octubre 6 de 2023
"""

#Cree un programa que lea una cantidad e imprima un porcentaje a calcular requerido sobre esa cantidad.

cant = float(input("Ingrese la cantidad: "))
porcen = float(input("Ingrese el porcentaje que desea calcular: "))
res = (porcen / 100) * cant
print(f"El {porcen}% de {cant} es {res:.2f}")