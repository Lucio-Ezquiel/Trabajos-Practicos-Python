'''
Escribe un programa que permita al usuario ingresar una lista y la invierta
'''




def ingresar_elemento():
    while True:
        return input("Ingresa un elemento de la lista: ")
    
def desea_continuar():
    while True:
        decision = input("¿Desea ingresar otro elemento? (s/n): ").strip().lower()
        if decision in ['s', 'n']:
            return decision == 's'
        print("Entrada no válida. Por favor, ingrese 's' para sí o 'n' para no.")

def invertir_lista(lista):
    return lista[::-1]

def main():
    elementos = []

    while True: 
        elemento = ingresar_elemento()
        elementos.append(elemento)

        if not desea_continuar():
            break

    elementosInvertidos = invertir_lista(elementos)
    print(f'Su lista de elementos es {elementos} \nSu lista invertida es {elementosInvertidos} ')

if __name__ == '__main__':
    main()

