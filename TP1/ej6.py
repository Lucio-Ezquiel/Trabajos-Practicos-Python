"""
6) Lee un número por teclado que pida el precio de un producto (puede tener
decimales) y calcule el precio final con IVA. El IVA sera una constante que sera del 21%
"""
numero = int(input("Ingrese un precio sin signo: "))
print("Precio final: ", (numero * 0.21) + numero)