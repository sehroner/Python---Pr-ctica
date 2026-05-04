repetir = "s"

while repetir != "n":
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    print(f"El resultado de la suma es: {num1 + num2}")
    repetir = input("Deseas repetir la operación s/n: ").lower()

print("Programa finalizado")
