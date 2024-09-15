"""
22- Suma los dígitos de un número ingresado por el usuario de forma recursiva.
Ejemplo: el usuario ingresa 1596
El programa debe sumar 1 + 5 + 9 + 6
"""
def recDigitos(numero):
    if len(numero) == 1:
         return int(numero)
    else:
         return recDigitos(numero[1:]) + int(numero[0])

num = input("Ingrese un numero: ")
print(recDigitos(num))
