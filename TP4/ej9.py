"""
Dado el siguiente texto:
texto = "manzana naranja manzana pera pera pera naranja manzana"
a) Escribe un programa que cuente cuántas veces aparece cada palabra en el
texto utilizando un diccionario.
b) Imprime el diccionario resultante.
"""

texto = "manzana naranja manzana pera pera pera naranja manzana"
conteo = {}

for word in texto.split(" "):
    if word not in conteo:
        conteo[word] = 1
    else:
        conteo[word] += 1

print(conteo)
