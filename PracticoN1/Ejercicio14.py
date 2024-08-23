import random

contador = 1
numAleatorio = random.randint(1, 100)
numIngresado = int(input("Introduce un numero entre 1 y 100: "))
print(numAleatorio)
while (numIngresado != numAleatorio):
    if (numIngresado > numAleatorio):
        print("El numero es menor")
        numIngresado = int(input("Introduce un numero entre 1 y 100: "))
    else:
        print("El numero es mayor")
        numIngresado = int(input("Introduce un numero entre 1 y 100: "))
    contador += 1

print("Encontraste el numero en", contador, "intentos")