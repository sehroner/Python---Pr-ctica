operador1=int(input("Introduce el primer valor: "))
operador2=int(input("Introduce el segundo valor: "))

if 0 <= operador1 <= 10 and 0 <= operador2 <= 10:
    if operador1 > operador2:
        print(f"El número {operador1} es mayor que el número {operador2}")

    elif operador2 > operador1:
        print("El número", operador2, "es mayor que el número", operador1)

    else:
        print("Ambos números son iguales")

else:
    print("Uno o los dos números están fuera de los límites establecidos")