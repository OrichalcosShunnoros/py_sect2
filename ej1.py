"""
Programa que calcula el area de un triángulo.
Autor: CZ
Fecha: 20 octubre de 2023
"""

#Cree un programa que tome la base y la altura de un triángulo e imprima su área.
#b*a/2=formula para hallar el área de un triángulo.


b = float(input("Ingresar la base: "))
al = float(input("Ingrese la altura: "))

a = 0.5 * b * al

print(f"El área de un triángulo con base {b} y altura {al} es igual a {a:.2f}")


