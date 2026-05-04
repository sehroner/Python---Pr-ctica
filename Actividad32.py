import random

lista = ['casa', 'barco', 'gato', 'perro', 'madera', 'agua', 'puente', 'pantalón']


palabra_secreta = random.choice(lista)
letras_desordenadas = list(palabra_secreta)
random.shuffle(letras_desordenadas)

print(letras_desordenadas)

intentos = 0
acertado = False

while intentos < 3 and not acertado:
    intento = input("Introduce palabra correcta: ")
    intentos += 1

    if intento == palabra_secreta:
        acertado = True
        print("Acertaste")
    else:
        print("no has acertado")

if not acertado:
    print("no has acertado ninguno de los intentos")
