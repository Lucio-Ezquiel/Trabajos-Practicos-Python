"""
10- Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario
pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el
resultado por pantalla.
"""
cad = input("Ingrese una cadena: ")
op = int(input("Ingrese 1 para mayusculas o 0 para minusculas"))
print(f"{(op and cad.upper()) or cad.lower()}")
