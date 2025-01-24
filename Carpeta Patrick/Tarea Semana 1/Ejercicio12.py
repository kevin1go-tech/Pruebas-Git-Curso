#Ejercicio 12
def calcular_cargo(horas):
    if horas <= 1:
        cargo = 3.00
    else:
        cargo = 3.00
        cargo += (horas - 1) * 0.50

    if cargo > 12.00:
        cargo = 12.00

    return cargo

horas = float(input("Ingrese el número de horas: "))

cargo_total = calcular_cargo(horas)
print(f"El cargo por {horas} horas de estacionamiento es: S/{cargo_total:.2f}")
