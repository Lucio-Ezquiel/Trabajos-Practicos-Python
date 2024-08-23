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
    tipoDia={
        1:"Laboral",
        2:"Laboral",
        3:"Laboral",
        4:"Laboral",
        5:"Laboral",
        6:"No Laboral",
        7:"No Laboral"
    }
    if dia in diasSemanas:
        print(diasSemanas(dia), "es un dia ", tipoDia(dia))
    else:
        print("El numero ingresado no es valido. Ingrese un numero del 1 al 7")
while True:
    try:
        dia=int(input("Ingrese un número del 1 al 7 para el día de la semana: "))
        esDiaLaboral(dia)
        break
    except ValueError:
        print("Ingrese un numero valido")