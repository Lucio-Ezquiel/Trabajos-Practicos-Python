"""
Cargar una Lista de números decimales de tamaño MXN y mostrar los datos
cargados. El tamaño de la Lista debe ser solicitado e ingresado por el usuario,
indicando un valor entero para las filas y un valor entero para las columnas, el
valor mínimo valido debe ser de 3x2, crear la Lista y solicitar los valores
numéricos para cargar de datos en cada posición. La carga de los datos puede ser 
manual, donde los datos serán ingresados por el usuario o aleatoria, donde los 
números serán generados automáticamente, ambos casos en el rango de 1 a 999. 
El sistema preguntara al usuario como quiere hacer la carga de valores.
"""
import random

while True:
    try:
        filas = int(input("Ingrese el número de filas (mínimo 3): "))
        columnas = int(input("Ingrese el número de columnas (mínimo 2): "))
        if filas >= 3 and columnas >= 2:
            break
        else:
            print("Las dimensiones deben ser al menos 3x2.")
    except ValueError:
        print("Por favor, ingrese números enteros.")

matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(0)
    matriz.append(fila)

while True:
    carga = input("¿Cómo desea cargar los datos? (manual/aleatorio): ").lower()
    if carga == "manual":
        for i in range(filas):
            for j in range(columnas):
                while True:
                    try:
                        valor = int(input(f"Ingrese el valor para la posición [{i+1}, {j+1}]: "))
                        if 1 <= valor <= 999:
                            matriz[i][j] = valor
                            break
                        else:
                            print("Valor fuera de rango. Ingrese un número entre 1 y 999.")
                    except ValueError:
                        print("Por favor, ingrese un número entero.")
        break
    elif carga == "aleatorio":
        for i in range(filas):
            for j in range(columnas):
                matriz[i][j] = random.randint(1, 999)
        break
    else:
        print("Opción inválida. Ingrese 'manual' o 'aleatorio'.")

print("La matriz cargada es:")
for fila in matriz:
    print(fila)

"""
Generar una nueva Lista de N filas por 1 columna que contenga en cada celda de
la columna la sumatoria de las celdas de cada una de las filas de la Lista cargada
en el punto 1.
"""
matriz2 = []
for fila in matriz:
    numero=0
    for i in fila:
        numero += i
    matriz2.append(numero)

print("La matriz sumatorio de filas es:")
for filas in matriz2:
    print(filas)

"""
Generar una nueva Lista de tamaño N filas por 2 columnas donde la primer
columna contenga los valores calculados en el punto 3 pero ordenados de
Mayor a Menor, y en la segunda columna asignar el valor de la fila que poseía
originalmente en la Lista del punto 3.
"""

sumas_con_indices = []
for i, fila in enumerate(matriz):
    suma = 0
    for elemento in fila:
        suma += elemento
    sumas_con_indices.append((suma, i))

n = len(sumas_con_indices)
for i in range(n):
    for j in range(0, n-i-1):
        if sumas_con_indices[j][0] < sumas_con_indices[j+1][0]:
            sumas_con_indices[j], sumas_con_indices[j+1] = sumas_con_indices[j+1], sumas_con_indices[j]

matriz3 = []
for suma, indice in sumas_con_indices:
    matriz3.append([suma, indice + 1]) 

print("La matriz ordenada por suma de filas y su índice original es:")
for fila in matriz3:
    print(fila)

"""
Finalmente sume los elementos de la columna 1 de la Lista del punto 5 y
muestre el resultado de la sumatoria por pantalla.
"""
columnaFinal = 0
sumar = 0

for fila in matriz3:
    sumar += fila[columnaFinal]

print("La suma de la columna es: ", sumar)