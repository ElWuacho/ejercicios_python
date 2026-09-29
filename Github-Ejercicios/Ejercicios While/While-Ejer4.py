bol = True

while bol:
    letra = input("Ingrese la inicial del genero (F o M): ")
    if (letra == "F"):
        print("El generado elegido es: Femenino")
        bol = False
    elif (letra == "M"):
        print("El generado elegido es: Masculino")
        bol = False