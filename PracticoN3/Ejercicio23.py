"""
Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique 
si una matriz es simétrica.
"""
matriz=[[1,2,3],[2,4,5],[3,5,6]]
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))] 

if matriz == transpuesta:
    print("Esta matriz es simétrica")
else:
    print("Esta matriz no es simétrica")