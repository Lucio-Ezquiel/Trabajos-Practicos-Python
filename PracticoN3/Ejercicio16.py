"""
Modifica el programa anterior para que imprima la suma de cada fila de la lista 
bidimensional. 
"""
matriz=[[1,2,3],[4,5,6],[7,8,9]]
for i, fila in enumerate(matriz):
    print(f"Suma de la fila {i+1}:{sum(fila)}")