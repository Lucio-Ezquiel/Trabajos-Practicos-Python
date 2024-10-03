"""
a) Cuenta cuántas veces aparece el número 4 en la tupla. 
b) Imprime el resultado. 
"""
numeros = (1, 2, 2, 3, 4, 4, 4, 5)
contador = 0

for num in numeros:
    if num == 4:
        contador = contador + 1

print("El número 4 aparece: ",contador,"veces")
