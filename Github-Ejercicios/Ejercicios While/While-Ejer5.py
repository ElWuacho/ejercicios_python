bol = True
total = 0
cont = 0
promedio = 0

while bol:
    numero = int(input("Ingrese un numero: "))
    total = total + numero
    cont = cont + 1
    if (cont == 5):
        bol = False

print(f"La suma de los numeros ingresados es: {total}")

promedio = total / cont

print(f"El promedio de los numeros ingresados es: {promedio}")

