def ingresar_numero():
    while True:
        try:
            return int(input("Ingrese un número: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def desea_continuar():
    while True:
        decision = input("¿Desea ingresar otro número? (s/n): ").strip().lower()
        if decision in ['s', 'n']:
            return decision == 's'
        print("Entrada no válida. Por favor, ingrese 's' para sí o 'n' para no.")

def main():
    numeros = []

    while True:
        numero = ingresar_numero()
        numeros.append(numero)
        
        if not desea_continuar():
            break

    suma = sum(numeros)
    print(f"La suma de los números ingresados es: {suma}")

if __name__ == "__main__":
    main()
