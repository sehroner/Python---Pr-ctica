total = 0
contador = 0

while total <= 50:
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    resultado = num1 + num2
    total += resultado
    contador += 1

    print(f"El resultado de la suma es: {resultado}")

    
    if contador == 1:
        print(f"El total acumulado es: {total} y llevas {contador} operación realizada")
    else:
        print(f"El total acumulado es: {total} y llevas {contador} operaciones realizadas")

print("Fin del programa")