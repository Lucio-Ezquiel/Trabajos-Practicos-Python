"""
Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido 
de las agujas del reloj.
"""
matriz=[[1,2,3],[4,5,6],[7,8,9]]
n=len(matriz)
rotada = [[0] * n for _ in range(n)]

for i in range(n):
        for j in range(n):
            rotada[j][n-i-1] = matriz[i][j]

print("La matriz rotada 90 grados es: ",rotada)