mensaje = input("Ingrese el nombre de un mes: ")

match mensaje:
    case "Julio" | "Agosto":
        print("Estamos en invierno aun!")
    case "Enero" | "Febrero" | "Marzo" | "Abril" | "Mayo" | "Junio":
        print("Todavia no llego el invierno!")
    case "Septiembre" | "Octubre" | "Noviembre" | "Diciembre":
        print("Ya paso el invierno!")
    case _:
        print("Dato ingresado no valido!")