
suma = 0
cinc = 0
nueve = 0
diez = 0
sumaCaracteres = 0

#Pedimos el numero al usuario (automaticamente esta en string), luego sacamos la longitud de esa cadena de texto utilizando len(num)
num = input("Ingrese un numero entero")
long = len(num)

caracteres = list(num)
print(caracteres)

for caracter in caracteres : 
    sumaCaracteres = sumaCaracteres + int(caracter)
    ultimoCaracter = int(caracter)

print(sumaCaracteres)
print(ultimoCaracter)

if int(num) % 2 == 0:
    print("El numero es divisible por 2")
if sumaCaracteres % 3 == 0:
    print("El numero es divisible por 3")
if ultimoCaracter == 5 or ultimoCaracter == 0:
    print("El numero es divisible por 5")
if int(num) % 2 == 0 and sumaCaracteres % 3 == 0:
    print("El numero es divisible por 6")
if sumaCaracteres % 9 == 0:
    print("El numero es divisible por 9")
if ultimoCaracter == 0:
    print("El numero es divisible por 10")




