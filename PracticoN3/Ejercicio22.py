"""
Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz 
identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa 
principal son 1 y el resto son 0. 
"""
n=int(input("Ingrese el tamaño de la matriz cuadrada bidimensional: "))
matrizIdentidadInversa = [[1 if i+j == n-1 else 0 for j in range(n)] for i in range(n)]
for fila in matrizIdentidadInversa: 
    print(fila)