"""
Escribe un programa que multiplique cada elemento de una lista bidimensional por un
valor escalar dado por el usuario.
"""
m = [[6, 12, 18], [5, 11, 17], [4, 10, 16], [3, 9, 15], [2, 8, 14], [1, 7, 13]]

v = int(input("Ingrese valor de la escalar: "))

for f in range(len(m)):
    for e in range(len(m[f])):
        m[f][e] = v*m[f][e]

print(m)
