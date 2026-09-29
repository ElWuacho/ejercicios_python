numero = int(input("Ingrese un numero: "))

for indice in range (1, numero):

    indice1 = indice

    total = indice1 % 2

    if (total != 1):
        print(indice1)