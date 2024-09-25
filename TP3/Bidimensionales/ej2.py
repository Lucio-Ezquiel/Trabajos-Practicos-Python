"""
Escribe un programa que calcule la suma de todos los elementos en una lista
bidimensional.
Pista: Aplique la función sum
"""
m = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

print(sum(sum(fila) for fila in m))
