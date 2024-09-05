"""
13- Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se
encuentra dentro de la primera.
"""
cad = input("Ingrese primer cadena: ")
search = input("Ingrese termino que buscar: ")

if search in cad:
    print("Encontrado.")
else:
    print("No encontrado.")
