operador1=int(input("Introduce el primer valor: "))
operador2=int(input("Introduce el segundo valor: "))

if operador1 > operador2:
    print(f"El número {operador1} es mayor que el número {operador2}")

if operador2 > operador1:
    print("El número", operador2, "es mayor que el número", operador1)

if operador1 == operador2:
    print("Ambos números son iguales")