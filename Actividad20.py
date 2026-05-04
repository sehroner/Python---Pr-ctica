pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
suma = 0

while True:
    num = int(input("Introduce un número: "))

    if num == -99:
        break

    suma += num

    if num == 0:
        ceros += 1
    elif num > 0:
        positivos += 1
    else:
        negativos += 1
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\nRESUMEN")
print("El número de pares es", pares)
print("El número de impares es", impares)
print("El número de positivos es", positivos)
print("El número de negativos es", negativos)
print("El número de ceros es", ceros)
print("El total es", suma)