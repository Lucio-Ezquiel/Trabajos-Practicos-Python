#Cargar una Lista de números decimales de tamaño MXN y mostrar los datos
#indicando un valor entero para las filas y un valor entero para las columnas, el
#valor mínimo valido debe ser de 3x2, crear la Lista y solicitar los valores
#numéricos para cargar de datos en cada posición. La carga de los datos puede ser 
#manual, donde los datos serán ingresados por el usuario o aleatoria, donde los 
#números serán generados automáticamente, ambos casos en el rango de 1 a 999. 
#El sistema preguntara al usuario como quiere hacer la carga de valores.
import random
matriz = []

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

while True:
    carga = input("¿Cómo desea cargar los datos? (manual/aleatorio): ").lower()
    if carga == "manual":
        for i in range(filas):
            fila = []
            for j in range(columnas):
               valor = int(input(f"Ingresa el valor para la posicion [{i+1},{j+1}]: "))
               if 1 <= valor <=999:
                   fila.append(valor)
               else:
                   print("Fuera de rango.")
            matriz.append(fila)
        break
    elif carga == "aleatorio":
        for i in range(filas):
            fila = []
            for i in range(columnas):
                fila.append(random.randint(1,999))
            matriz.append(fila)
        break
                   
#Mostrar la Lista resultante por pantalla en formato de Lista (filas y columnas).
for fila in matriz:
    print(fila)        

#Generar una nueva Lista de N filas por 1 columna que contenga en cada celda de
#la columna la sumatoria de las celdas de cada una de las filas de la Lista cargada
#en el punto 1.
matriz2 = []
for fila in matriz:
    suma=0
    for i in fila:
       suma += i
    matriz2.append(suma)

#Mostrar la Lista resultante por pantalla.
for fila in matriz2:
    print(fila)

#Generar una nueva Lista de tamaño N filas por 2 columnas donde la primer
#columna contenga los valores calculados en el punto 3 pero ordenados de
#Mayor a Menor, y en la segunda columna asignar el valor de la fila que poseía
#originalmente en la Lista del punto 3.
matriz_tres = []
tamaño = len(matriz2)

while tamaño > 0:
    mayor = 0
    posicion = 0
    for i, fila in enumerate(matriz2):
        if fila > mayor:
            mayor = fila
            posicion = i
    #A la matriz numero 3 le mando como primera fila la fila mayor y la posicion en la que esta
    matriz_tres.append([mayor, posicion])
    #Indicamos que en la matriz2 y en la posicion que se encuentra, estos no se van a tomar en cuenta para el proximo bucle
    matriz2[posicion] = -1
    #Le restamos tamaño a la matriz para que cuando se terminen de ordenar todos los valores el bucle while termine
    tamaño -=1
    
#Mostrar la Lista resultante por pantalla.

for fila in matriz_tres:
    print(fila)

#Finalmente sume los elementos de la columna 1 de la Lista del punto 5 y
#muestre el resultado de la sumatoria por pantalla.

suma_elementos = 0

for fila in matriz_tres:
   suma_elementos += fila[0]

print(suma_elementos)
