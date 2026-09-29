
print("1- Enero")
print("2- Marzo")
print("3- Julio")
print("4- Diciembre")

mensaje = int(input("Ingrese un numero del mes: "))

match mensaje:
    case 1:
        print("Que comiences bien el año!")
    case 2:
        print("A clases!")
    case 3:
        print("Se vienen las vacaciones!")
    case 4:
        print("Felices fiestas!")
    case _:
        print("Dato ingresado no valido!")