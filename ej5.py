"""
Programa que calcula el descuento del 10% para un producto.
Autor: Christian Zambrano
Fecha: Octubre 6 de 2023
"""

#Cree un programa que tome el valor de un producto e imprima su precio final si este siempre tiene un valor del 10% de descuento.

val_prod = float(input("Ingrese el valor del producto: $"))
desc = 0.10 
desc_apli = val_prod * desc
val_fin = val_prod - desc_apli
print(f"El precio final con un descuento del 10% es: ${val_fin:.2f}")