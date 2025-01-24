#Ejercicio 10
aprobadas = []
desaprobadas = []

while True:
    nota = float(input("Ingrese una nota: "))

    if nota >= 11:
        aprobadas.append(nota)
    else:
        desaprobadas.append(nota)

    respuesta = input("¿Desea seguir ingresando notas? (Sí/SÍ/sí para continuar): ").lower()

    if respuesta not in ['sí', 'sí', 'si']:
        break

print("\nNotas aprobadas:", aprobadas)
print("Notas desaprobadas:", desaprobadas)
