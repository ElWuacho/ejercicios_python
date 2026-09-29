mensaje = input("Ingrese el nombre de un mes: ")

match mensaje:
    case "Febrero":
        print("Este mes no tiene 29 dias!")
    case "Enero" | "Marzo" | "Abril" | "Mayo" | "Junio" | "Julio" | "Agosto" | "Septiembre" | "Octubre" | "Noviembre" | "Diciembre":
        print("Este mes tiene 30 dias o mas!")
    case _:
        print("Dato ingresado no valido!")