lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

total = len(lista1)
numeros = 0
letras = 0
mayusculas = 0
suma = 0

for elemento in lista1:
    if elemento.isnumeric():
        numeros += 1
        suma += int(elemento)
    elif elemento.isalpha():
        letras += 1
        if elemento.isupper():
            mayusculas += 1

print(f"Número de valores: {total}")
print(f"Cantidad de números: {numeros}")
print(f"Cantidad de letras: {letras}")
print(f"Cantidad de mayúsculas: {mayusculas}")
print(f"Suma total de números: {suma}")