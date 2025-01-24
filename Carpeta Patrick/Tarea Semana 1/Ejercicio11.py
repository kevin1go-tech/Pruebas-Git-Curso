#Ejercicio 11
asignaturas = []

for i in range(5):
    asignatura = input(f"Ingrese el nombre de la asignatura {i+1}: ")
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    asignaturas.append((asignatura, nota))

for asignatura, nota in asignaturas:
    print(f"En la asignatura {asignatura} sacó {nota}.")
