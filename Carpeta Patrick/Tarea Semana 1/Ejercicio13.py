#Ejercicio 13
def es_multiplo(a, b):
    if a % b == 0:
        print(f"{a} es múltiplo de {b}.")
    else:
        print(f"{a} no es múltiplo de {b}.")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

es_multiplo(numero1, numero2)