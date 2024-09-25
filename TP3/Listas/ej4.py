"""
Escribe un programa que pida al usuario una lista de números y cuente cuántos de
ellos son pares y cuántos son impares.
"""

def check(list):
    odd = 0
    even = 0
    for item in list:
        if item % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print("Presione q para terminar de ingresar numeros.")
lista = []
while True:
    n = input("Ingrese un numero o q: ")
    if n == "q":
        break
    lista.append(int(n))
par, impar = check(lista)
print(f"Par: {par}, Impar: {impar}")
