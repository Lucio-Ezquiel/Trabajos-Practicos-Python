import random
""
numIngresado = 0
contador = 1
numAleatorio = random.randint(1, 100)
print(numAleatorio)
while (numIngresado != numAleatorio):
    numIngresado = int(input("Introduce un numero entre 1 y 100: "))
    if (numIngresado > numAleatorio):
        print("El numero es menor")
    else:
        print("El numero es mayor")
    contador += 1

print("Encontraste el numero en", contador, "intentos")