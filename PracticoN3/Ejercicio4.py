"""
Escribe un programa que pida al usuario una lista de números y cuente cuántos de 
ellos son pares y cuántos son impares. 
"""
listaNum = []
n = int(input("Ingrese la cantidad de números que va a tener la lista: "))

for i in range(n):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    listaNum.append(numero)

pares = [x for x in listaNum if x % 2 == 0] 
impares = [x for x in listaNum if x % 2 !=0]   
     
print("La cantidad de números pares de la lista es: ", len(pares))
print("La cantidad de numeros impares de la lista es: ", len(impares))

