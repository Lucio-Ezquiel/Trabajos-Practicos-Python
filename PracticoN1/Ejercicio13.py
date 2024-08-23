num = input("ingrese un numero distinto de 1 para ver si es primo.")
suma = 0
num = int(num)

for i in range(1,num + 1):
    print(suma)
    if num % i == 0:
        suma = suma + 1

print(suma)

if suma == 2:
    print("numero primo")
else:
    print("numero no primo")




