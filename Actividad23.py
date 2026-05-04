repetir = "s"
suma_total = 0
contador = 0

while repetir != "n":
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
    suma_total += resultado
    contador += 1
    
    repetir = input("Deseas repetir la operación s/n: ").lower()

print("Resumen:")
print(f"la suma total es: {suma_total} y el número de repeticiones es: {contador}")