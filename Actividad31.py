import random

lista = ['casa', 'barco', 'gato', 'perro', 'madera', 'agua', 'puente', 'pantalón']

palabrasecreta = random.choice(lista)
acertado = False

while not acertado:
    intento = input("Introduce la palabra secreta: ")

    if intento == palabrasecreta:
        acertado = True
        print("ACERTASTE")
    else:
        print("SIGUE JUGANDO")
