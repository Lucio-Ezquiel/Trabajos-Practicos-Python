#Creo una variable número, le asigno un valor entero, y con el input a parte de mandar un mensaje, guardo el valor en número.
número = int(input("Ingrese un número por teclado"))

#Con este if comparo si el número y 2 son divisibles viendo si su resto es 0 o no.
if número % 2 == 0:
    print(número, "es divisible por 2.")
else:
    print(número, "no es divisible por 2.")