"""
Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una
matriz intercambia sus filas por columnas.
"""
m = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

def transpuesta(matriz):
    mt = []
    for c in range(len(matriz[0])):
        mt.append([])
        for f in range(len(matriz)):
            mt[c].append(matriz[f][c])
    return mt

print(transpuesta(m))
