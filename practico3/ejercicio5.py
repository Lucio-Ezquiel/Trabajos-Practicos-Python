'''
Escribe un programa que multiplique cada elemento de una lista de números por un valor ingresado por el usuario
'''

def main():
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    multiplo = int(input(f"Ingresar un valor para multiplicar la siguiente lista: {lista}: "))
    
    multiplos = [numero * multiplo for numero in lista ]
    
    print(f'La lista {lista} al multiplicarle cada valor por {multiplo} es igual a {multiplos}')
    
if __name__ == '__main__':
    main()