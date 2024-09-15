"""
23- Crea un programa donde se pida el ingreso de una cadena y por medio de
recursión mostrar la cadena de forma inversa.
Ejemplo: Ingreso “computadora de escritorio”
Invertir cadena “oirotircse ed arodatupmoc”
"""
def invertirCadena(cad):
    if len(cad) == 1:
        return cad
    else:
        return invertirCadena(cad[1:]) + cad[0]

cad = input("Ingrese un string: ")
print(invertirCadena(cad))
