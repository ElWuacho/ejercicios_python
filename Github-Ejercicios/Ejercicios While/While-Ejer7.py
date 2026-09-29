bol = True

multi = 0
positivo = 0
negativo = 1

while bol:

    numero = int(input("Ingrese un numero: "))

    if (numero > 0):

        positivo = positivo + numero

    else:

        negativo = negativo * numero

    palanca = input("Desea continuar operando? [Y/N]: ")

    if (palanca == "N"):

        bol = False

    print("Seguimos...")

print(f"La cantidad de numeros positivos son: {positivo}")
print(f"La cantidad de numero negativos son: {negativo}")
