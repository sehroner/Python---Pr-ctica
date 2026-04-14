import math

num1 = float(input("Introduce el primer valor: "))
num2 = float(input("Introduce el segundo valor: "))
num3 = float(input("Introduce el tercer valor: "))

operacion = num2**2 - 4*num1*num3

if operacion < 0:
    print("La raíz no puede ser un valor negativo")

else:
    x1 = (-num2 + math.sqrt(operacion)) / (2*num1)
    x2 = (-num2 - math.sqrt(operacion)) / (2*num1)

    print("El valor de x1 es:", x1)
    print("El valor de x2 es:", x2)