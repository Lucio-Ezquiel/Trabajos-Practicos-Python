"""
Crea un programa que lea una cadena de texto carácter por carácter usando 
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
def textoVertical(cadena, i=0):
    if i == len(cadena):
        return
    else:
        print(cadena[i])
        textoVertical(cadena, i + 1)

cadena = str(input("Ingrese una cadena de caracteres para ser mostrados por pantalla de forma vertical: "))
print(textoVertical(cadena))