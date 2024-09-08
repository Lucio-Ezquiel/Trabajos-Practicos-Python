"""
Escribe un programa que permita al usuario ingresar una lista y un número, y cuente 
cuántas veces aparece ese número en la lista.
"""
listaNum = []
numeroRepetido = {}
n = int(input("Ingrese la cantidad de números que va a tener la lista: "))
unNumero = int(input("Ingrese un número: "))

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    listaNum.append(numero)

for numero in listaNum:
    if numero in numeroRepetido:
        numeroRepetido[numero]+=1
    else:
        numeroRepetido[numero]=1

print("El número", unNumero, "aparece en la lista", numeroRepetido[unNumero], "veces")