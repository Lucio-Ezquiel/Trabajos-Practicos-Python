"""
Escribe un programa que permita al usuario ingresar una lista de números y filtre los
números primos.
Pista:
Usa una función para verificar si un número es primo.
"""

def check(numero):
        if numero > 1:
            for j in range(2,numero//2+1):
                if numero % j == 0:
                   return False 
            else:
                return True

print("Presione q para terminar de ingresar numeros.")
lista = []
while True:
    n = input("Ingrese un numero o q: ")
    if n == "q":
        break
    lista.append(int(n))
print([num for num in lista if check(num)])
