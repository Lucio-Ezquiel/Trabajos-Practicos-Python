"""
Escribe un programa que encuentre el valor más grande en una lista bidimensional.
"""
matriz=[[1,2,3],[4,10,6],[7,8,9]]
valorMax = max(max(fila) for fila in matriz )
print("El valor más grande de la lista bidimensional es: ", valorMax)