def esDiaLaboral(dia):
    diasSemanas={
        1:"Lunes",
        2:"Martes",
        3:"Miercoles",
        4:"Jueves",
        5:"Viernes",
        6:"Sabado",
        7:"Domingo"
    }
    if dia in diasSemanas:
        if 1<= dia <=5:
            print(diasSemanas(dia), "es un dia laboral")
        else:
            print(diasSemanas(dia),"No es un dia laboral")
    else:
        print("El dia ingresado no es valido, ingrese un numero del 1 al 7")
while True:
    try:
        dia=int(input("Ingrese un número del 1 al 7 para el día de la semana: "))
        esDiaLaboral(dia)
        break
    except ValueError:
        print("Ingrese un numero valido")