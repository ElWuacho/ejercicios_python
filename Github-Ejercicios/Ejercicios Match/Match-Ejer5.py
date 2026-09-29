numero = int(input("Ingrese un numero de la hora: "))

match numero:
    case 7 | 8 | 9 | 10 | 11:
        print("Todavia es horario de mañana!")
    case _:
        print("Dato ingresado no valido!")