#Ejercicio 1
import math
chocolates = int(input("Ingresé la cantidad de chocolates que se producirá al día: "))
chocoxsemana = chocolates * 7
cajas = math.ceil(chocoxsemana / 12)
print("José debe pedir", cajas, "cajas para la siguiente semana.")