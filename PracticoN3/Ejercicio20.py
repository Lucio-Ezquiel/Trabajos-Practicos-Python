"""
Escribe un programa que extraiga los elementos de la diagonal principal de una matriz 
cuadrada. 
"""
matriz=[[1,2,3],[4,5,6],[7,8,9]]
n=len(matriz)
diagonal=[matriz[i][i] for i in range(n)]
print("La diagonal principal de la matriz cuadrada es: ",diagonal)