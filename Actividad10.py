letra = input("Introduce una letra: ")

if letra.isalpha():
    if letra.islower():
        print("La letra es minúscula")

    if letra.isupper():
        print("La letra es mayúscula")

else:
    print("La letra es mayúscula ¿?")