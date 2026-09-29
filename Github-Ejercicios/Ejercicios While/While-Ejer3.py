bol = True

while bol:
    numero = int(input("Ingrese un numero: "))
    if (numero >= 0 and numero <= 9):
        print(numero)
        bol = False