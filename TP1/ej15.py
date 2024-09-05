"""
15) Dados los siguientes criterios de divisibilidad:
Criterios de divisibilidad del 2
Para saber si un número es divisible entre dos hay que comprobar que sea pa r
Criterios de divisibilidad del 3
Sumamos las cifras del número y si el resultado de la suma es un número
múltiplo de 3, entonces el número sí es divisible por 3.
Ejemplo
Como ya sabemos que 45 es divisible por 3 vamos a comprobar que la suma de
sus cifras es un múltiplo de 3.
Sumamos sus cifras: 45 –> 4 + 5 = 9
9 es divisible por 3 por lo tanto 45 también es divisible por 3.
Criterio de divisibilidad del 5
Para saber si un número es divisible entre 5, dicho número tiene que acabar en
0 o 5
Criterios de divisibilidad del 6
Si se cumplen los criterios del 2 y del 3, entonces también es divisible por 6
Criterio de divisibilidad del 9
Un número es divisible entre 9 cuando la suma de sus dígitos es 9 o múltiplo de
9.
Por ejemplo, vamos a comprobar si 2610 es un múltiplo de 9.
2 + 6 + 1 + 0 = 9, por lo tanto 2610 es divisible por 9.
Criterio de divisibilidad del 10
Para saber si un número es divisible entre 10, éste tiene que acabar en 0 .
Codifique un programa en Python que solicite el ingreso de un número entero y
determine cuáles son los criterios de divisibilidad que cumple.
"""
def c2(n):
    if (n % 2 == 0):
        return True
    else:
        return False

def c3(n):
    s = 0
    while n:
        s += n % 10 #grab last diget
        n //= 10    #remove last diget
    if (s % 3 == 0):
        return True
    else:
        return False

def c5(n):
    if (n % 10 == 0 or n % 10 == 5):
        return True
    else:
        return False

def c6(n):
    if (c2(n) and c3(n)):
        return True
    else:
        return False

def c9(n):
    s = 0
    while n:
        s += n % 10 #grab last diget
        n //= 10    #remove last diget
    if (s % 9 == 0):
        return True
    else:
        return False

def c10(n):
    if (n % 10 == 0):
        return True
    else:
        return False

n = int(input("Ingrese un numero: "))
print(f"c2: {c2(n)}")
print(f"c3: {c3(n)}")
print(f"c5: {c5(n)}")
print(f"c6: {c6(n)}")
print(f"c9: {c9(n)}")
print(f"c10: {c10(n)}")
