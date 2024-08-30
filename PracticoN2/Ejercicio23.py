"""
Crea un programa donde se pida el ingreso de una cadena y por medio de 
recursión mostrar la cadena de forma inversa.  
Ejemplo: Ingreso “computadora de escritorio”  
Invertir cadena “oirotircse ed arodatupmoc” 
"""
def cadenaInversa(cadena):
    #El slicing [::-1] indica que queremos tomar todos los elementos de la cadena (el primer :), pero en orden inverso (el segundo : y el -1).
    cadenaInvertida = cadena[:: -1]
    return cadenaInvertida

cadena = str(input("Ingrese una cadena: "))
print("La cadena de forma inversa es: ", cadenaInversa(cadena))