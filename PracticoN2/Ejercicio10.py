# Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario  pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el resultado por pantalla. 

cadena = str(input("Ingresa una cadena: "))
letra = str(input("Ingresa M para convertir a mayúsculas y m para convertir en minúsculas: "))

if letra == "M":
    print(cadena.upper())
else:
    print(cadena.lower())