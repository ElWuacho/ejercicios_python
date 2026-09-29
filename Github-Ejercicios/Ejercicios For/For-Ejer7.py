#ingrese un numero y determine si es numero primo, mostrar
numero = int(input("Ingrese un numero: "))

contador = 0

for indice in range (1, numero + 1):
    if numero % indice == 0:
        contador = contador + 1
if contador == 2:
    print("El numero es primo")
else:
    print("El numero no es primo")