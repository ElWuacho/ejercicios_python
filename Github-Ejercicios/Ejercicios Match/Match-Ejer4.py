mensaje = input("Ingrese el nombre de un mes: ")

match mensaje:
    case "Febrero":
        print("Este mes tiene 28 dias!")
    case "Abril" | "Junio" | "Septiembre" | "Noviembre":
        print("Este mes tiene 30 dias!")
    case "Enero" | "Marzo" | "Julio" | "Agosto" | "Octubre" | "Diciembre":
        print("Este mes tiene 31 dias!")
    case _:
        print("Dato ingresado no valido!")