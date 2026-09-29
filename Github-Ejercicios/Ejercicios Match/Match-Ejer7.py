numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

print("""
Ingrese la opcion que desea aplicar:
1 - Sumar.
2 - Restar.
3 - Multiplicar
4 - Dividir
""")

opcion = int(input("Ingrese la opcion: "))

match opcion:
    case 1:
        total = numero1 + numero2
        print(f"La suma de ambos numeros es: {total}")
    case 2:
        total = numero1 - numero2
        print(f"La resta da un total de: {total}")
    case 3:
        total = numero1 * numero2
        print(f"La multiplicacion da un total de: {total}")
    case 4:
        total = numero1 / numero2
        total = round(total, 2) # limita el resultado hasta 2 decimales en este ejemplo
        print(f"La division es un total de: {total}")
    case _:
        print("La opcion no es valida")