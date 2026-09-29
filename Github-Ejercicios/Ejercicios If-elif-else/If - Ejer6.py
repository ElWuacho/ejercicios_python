numero = input("ingrese un numero: ")
numero = int(numero)

if (numero > 17):
    print("La persona es mayor de edad.")
elif (numero <= 17 and numero >= 13):
    print("La persona es adolescente.")
else:
    print("La persona es un niño.")