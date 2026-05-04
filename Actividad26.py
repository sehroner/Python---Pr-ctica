import random

nombres = {1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis"}
contadores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for x in range(100):
    resultado = random.randint(1, 6)
    contadores[resultado] += 1

for numero, nombre in nombres.items():
    print(f"{nombre}: {contadores[numero]}")