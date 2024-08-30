# Pedir el ingreso de dos cadenas por teclado, indicar si la segunda cadena se encuentra dentro de la primera.

cadena1 = str(input("Ingrese su primer cadena: "))
cadena2 = str(input("Ingrese su segunda cadena: "))

#El operador in devuelve True si la subcadena está presente en la cadena más larga y False en caso contrario.
if cadena2 in cadena1:
    print("La segunda cadena se encuentra dentro de la primera")
else:
    print("La segunda cadena no se encuentra dentro de la primera")