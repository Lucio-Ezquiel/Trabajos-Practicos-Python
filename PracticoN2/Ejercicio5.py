#Solicite el ingreso de una cadena y elimine todos los espacios de la misma, muestre la cadena resultante.

def eliminarEspacios(cadena):
    return cadena.replace(" ", "")

cadena = str(input("Ingrese una frase: "))
cadena1 = eliminarEspacios(cadena)
print(cadena1)