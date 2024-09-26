"""
Escribe un programa que calcule la suma de todos los elementos en una lista 
bidimensional. 
Pista: Aplique la función sum 
"""
matriz=[[1,2,3],[4,5,6],[7,8,9]]
resultado = sum(sum(fila) for fila in matriz)
print("El resultado de la suma de los elementos de la matriz bidimensional es: ",resultado)