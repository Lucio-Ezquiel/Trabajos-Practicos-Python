"""
Escribe un programa que multiplique cada elemento de una lista de números por un
valor ingresado por el usuario.
"""
lista = [1,2,3,4,5,6]

c = int(input("Ingrese un numero multiplicador: "))
print([num*c for num in lista])
