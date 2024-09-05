"""
14) Codifique un programa de consola en Java que permita realizar las siguientes
acciones:
Generar un número aleatorio entre 0 y 100, para ello use la siguiente función:
random.randint(0, 100)
Una vez generado el número codifique la lógica necesaria para encontrar el número
aleatorio ayudando al usuario informando al mismo si el número ingresado es mayor o
menor al número aleatorio buscado. Una vez encontrado el número muestre la
cantidad de intentos necesarios para lograrlo.
Ejemplo: Número aleatorio generado: 63
Ingrese un número entre 0 y 100.
Numero Ingresado: 50
Respuesta: Es muy bajo
Ingrese un número entre 0 y 100.
Numero Ingresado: 75
Respuesta: Es muy alto
Ingrese un número entre 0 y 100.
Numero Ingresado: 60
Respuesta: Es muy bajo
Ingrese un número entre 0 y 100.
Numero Ingresado: 65
Respuesta: Es muy alto
Ingrese un número entre 0 y 100.
Numero Ingresado: 63
Respuesta: Correcto, numero encontrado, cantidad de intentos 5
"""
import random

def genN():
    return random.randint(0, 100)
n = genN()
c = 1
while True:
    g = int(input("Ingrese un numero entre 0 y 100. "))
    print("Numero ingresado:", g)
    if g > n:
        print("Repuesta: Es muy alto.")
    elif g < n:
        print("Repuesta: Es muy bajo.")
    else:
        print("Repuesta: Correcto, numero encontrado, cantidad de intentos: ",c)
        break
    c += 1
