lista = []
repetir = "s"

while repetir != "n":
    letra = input("Introduce una letra: ")

    if letra.isalpha():
        if letra not in lista:
            lista.append(letra)
    else:
        print("No es una letra válida, inténtalo de nuevo.")

    repetir = input("¿Deseas repetir s/n?: ").lower()

print(lista)