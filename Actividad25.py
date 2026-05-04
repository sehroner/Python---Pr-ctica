import random

numero = random.randint(1, 1000)
intentos = 0
acertado = False

while not acertado:
    intento = int(input("Introduce un valor comprendido entre 1 y 1000: "))

    if intento < 1 or intento > 1000:
        print("El número debe estar entre 1 y 1000")
        continue

    intentos += 1

    if intento < numero:
        print("El número que has introducido es menor")
    elif intento > numero:
        print("El número que has introducido es mayor")
    else:
        acertado = True

print(f"Acertaste, has realizado {intentos} intentos")