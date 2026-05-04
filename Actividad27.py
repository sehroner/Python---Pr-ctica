cantidad = int(input("¿Cuántos números quieres introducir?: "))

numeros = []

for x in range(cantidad):
    numero = int(input("Introduce un número: "))
    numeros.append(numero)

numeros.sort()
print(numeros)