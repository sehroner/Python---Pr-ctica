a = int(input("Introduce el primer intervalo: "))
b = int(input("Introduce el segundo intervalo: "))

if a < b:
    for x in range(a, b + 1):
        if x == b:
            print(x)
        else:
            print(x, end="-")

else:
    for x in range(a, b - 1, -1):
        if x == b:
            print(x)
        else:
            print(x, end="-")