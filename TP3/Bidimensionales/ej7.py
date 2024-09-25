"""
Escribe un programa que extraiga los elementos de la diagonal principal de una matriz
cuadrada.
"""
m = [[6, 12, 18], [5, 11, 17], [4, 10, 16]]
n = []

for i in range(min(len(m), len(m[0]))):
    n.append(m[i][i])

print(n)
