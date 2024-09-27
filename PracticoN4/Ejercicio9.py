"""
a) Escribe un programa que cuente cuántas veces aparece cada palabra en el 
texto utilizando un diccionario. 
b) Imprime el diccionario resultante.
"""
texto = "manzana naranja manzana pera pera pera naranja manzana"
palabra = texto.split()
diccionario = {}

for pal in palabra:
    if pal in diccionario:
        diccionario[pal] += 1
    else:
        diccionario[pal] = 1

print(diccionario)