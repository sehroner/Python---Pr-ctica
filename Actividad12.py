letra = input("Introduce una letra: ")

if letra.islower():
    print("La letra es minúscula")

elif letra.isupper():
    print("La letra es mayúscula")

elif letra.isnumeric():
    print("El valor introducido es un número")

else:
    print ("El valor introducido es un símbolo")