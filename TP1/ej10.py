"""
10) Lee un número por teclado y comprueba que este número es mayor o igual que
cero, si no lo es lo volverá a pedir (do while), después muestra ese número por
consola.
"""
while True:
    i = int(input("Ingrese un numero: "))
    if (i >= 0):
        break

print(i)