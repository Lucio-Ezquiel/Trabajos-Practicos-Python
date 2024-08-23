
suma = 0
cinc = 0
nueve = 0
diez = 0

num = input("Ingrese un numero entero")
if len(num) == 2 :
    suma = int(num[0]) + int(num[1])
elif len(num) == 1:
    suma = int(num)
elif len(num) == 3:
    suma = int(num[0]) + int(num[1]) + int(num[2])

if len(num) == 2 :
    cinc = int(num[1])
elif len(num) == 3 :
    cinc = int(num[2])

if len(num) == 2:
   nueve = int(num[0]) + int(num[1])
elif len(num) == 3:
    nueve = int(num[0]) + int(num[1]) + int(num[2])
elif len(num) == 1:
    nueve = int(num)

if len(num) == 2:
    diez = int(num[1])
elif len(num) == 3:
    diez = int(num[2])
    
if int(num) % 2 == 0:
    print("El numero es divisible por 2")
if suma % 3 == 0:
    print("El numero es divisible por 3")
if cinc == 0 or cinc == 5 or int(num) == 0 or int(num) == 5:
    print("El numero es divisible por 5")
if int(num) % 2 == 0 and suma % 3 == 0:
    print("El numero es divisible por 6")
if nueve % 9 == 0:
    print("El numero es divisible por 9")
if diez == 0:
    print("El numero es divisible por 10")