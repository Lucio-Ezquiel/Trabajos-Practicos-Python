#Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII. Muéstralos en línea recta, separados por un espacio entre cada carácter.  

cadena = "La lluvia de Mendoza es escasa"

for caracter in cadena:
    #La función ord() toma un carácter como entrada y devuelve su correspondiente valor ASCII.
    codigoAscii = ord(caracter)
    print(codigoAscii, end=" ")
