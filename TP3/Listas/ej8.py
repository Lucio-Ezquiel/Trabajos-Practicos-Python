"""
Escribe un programa que identifique y muestre los elementos que se repiten en una
lista.
"""
lista = [1,2,3,4,5,6,3,4,5,7]

for i in set(lista):
    lista.remove(i)

print(list(set(lista)))
