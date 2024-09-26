"""
Escribe un programa que identifique y muestre los elementos que se repiten en una 
lista. 
Pista: 
 Utiliza un diccionario o un conjunto (set) para hacer el seguimiento de los 
elementos.
"""
listaNum = [1, 2, 2, 3, 3, 4, 5]
contador= {}

for num in listaNum:
    contador[num] = contador.get(num, 0) + 1

print("Elementos repetidos:", end=" ")
for num, veces in contador.items():
    if veces > 1:
        print(num, end=" ")   