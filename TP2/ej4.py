"""
4- Desarrolle un programa que ayude a una cajera a determinar el número de billetes y
monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50,
20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de
dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete
de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05
centavos. Plantee el algoritmo planteando métodos para su resolución.
"""
while True:
    try:
        n = float(input("Ingrese monto: "))
    except:
        print("Error con monto ingresado.")
    if n: break

bills = [200, 100, 50, 20, 10, 5, 2, 1]
coins = [0.50, 0.25, 0.10, 0.05]
change = {}

# bills first
for bill in bills:
    if int(n // bill):
        change[bill] = int(n // bill)
        n = n % (change[bill] * bill)

# coins
for coin in coins:
    if int(n // coin):
        change[coin] = int(n // coin)
        n = n % (change[coin] * coin)

print(change)
