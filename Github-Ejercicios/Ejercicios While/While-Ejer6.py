bol = True
cont = 0
promedio = 0
total = 0

while bol:

    numero = int(input("Ingrese su numero por favor: "))

    total = total + numero

    cont = cont + 1

    palanca = input("¿Quiere agregar mas numeros? (Y/N): ")

    if (palanca == "N"):

        print("Fin de ciclo.")
        bol = False

promedio = total / cont

print(f"La suma total de los numeros es: {total}\nY el promedio es: {promedio}")