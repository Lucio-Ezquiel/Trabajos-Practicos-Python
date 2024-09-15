"""
24- Crea un programa que lea una cadena de texto carácter por carácter usando
recursión.
Ejemplo: Ingreso “UTN FRM Mza”
Salida: U
T
N
F
R
M
M
z
a
"""
def prntCadena(cad):
    print(cad[0])
    if len(cad) != 1:
        prntCadena(cad[1:])

cad = input("Ingrese un string: ")
prntCadena(cad)
