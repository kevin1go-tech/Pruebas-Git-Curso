#Ejercicio 14
def convertir_a_segundos(horas, minutos, segundos):
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos

horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

total_segundos = convertir_a_segundos(horas, minutos, segundos)
print(f"El equivalente en segundos es: {total_segundos} segundos.")
