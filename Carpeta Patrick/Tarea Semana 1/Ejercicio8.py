#Ejercicio 8
num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

while (num1 < num2):
  print("Error: El segundo número no debe ser mayor al primer número")
  num2 = int(input("Ingrese el segundo numero entero de nuevo: "))

print("Tus numeros son {} y {} xd".format(num1, num2))