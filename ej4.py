"""
Programa que calcula el precio final con un IVA de 19% de un producto
Autor: Christian Zambrano
Fecha: Octubre 6 de 2023
"""

#Cree un programa que tome el precio de un producto e imprima su precio final al consumidor con un iva del 19%.

val_prod = float(input("Ingrese el precio del producto: $"))
iva = 0.19
val_prod_iva = val_prod + (val_prod * iva)
print(f"El precio final con un 19% de IVA es: ${val_prod_iva:.2f}")