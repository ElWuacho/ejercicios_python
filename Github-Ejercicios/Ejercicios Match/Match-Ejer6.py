mensaje = int(input("Ingrese un numero de la hora: "))

match mensaje:
    case 7 | 8 | 9 | 10 | 11:
        print("Es de mañana.")
    case 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19:
        print("Es de tarde.")
    case 20 | 21 | 22 | 23:
        print("Es de noche.")
    case _:
        print("La hora no existe!")