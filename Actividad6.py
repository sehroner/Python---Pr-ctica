peso = float(input("Introduce el peso(kg): "))
altura = float(input("Introduce la altura(m): "))

imc = peso / (altura ** 2)

if imc >= 25:
    print(f"Si pesas {peso} kilos y mides {altura}, tu IMC es: {round(imc,2)}. Hay sobrepeso")

else:
    print(f"Si pesas {peso} kilos y mides {altura}, tu IMC es: {round(imc,2)}")
