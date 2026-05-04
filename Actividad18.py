palabra = input("Introduce una palabra: ")

vocales = ""
consonantes = ""

for letra in palabra:
    if letra.lower() in "aeiouáéíóú":
        vocales += letra
    elif letra.isalpha():
        consonantes += letra

print("Las vocales de la palabra", palabra, "son: ", vocales)
print("Las consonantes de la palabra", palabra, "son: ", consonantes)