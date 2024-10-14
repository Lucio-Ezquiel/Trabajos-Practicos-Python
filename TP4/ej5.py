"""
Dada la siguiente tupla:
numeros = (1, 2, 2, 3, 4, 4, 4, 5)
a) Cuenta cuántas veces aparece el número 4 en la tupla.
b) Imprime el resultado.
"""

numeros = (1, 2, 2, 3, 4, 4, 4, 5)
# print(numeros.count(4))
c = 0
for elem in numeros:
    if elem == 4:
        c += 1

print(f"4 aparece {c} veces en la tupla.")
