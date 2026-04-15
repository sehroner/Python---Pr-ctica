pares = 0
impares = 0

for x in range(1,51):
    if x % 2 == 0:
        pares += 1
    else:
        impares += 1

print("El total de pares es", pares, "El total de impares es: ", impares)