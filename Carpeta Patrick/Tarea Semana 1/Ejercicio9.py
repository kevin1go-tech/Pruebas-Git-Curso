#Ejercicio 9
num = int(input("Ingrese el numero: "))
numa = int(input("Ingrese el numero otra vez: "))
while (num < numa):
  num = numa
  numa = int(input("Ingrese el numero otra vez: "))

print("Game Over, el valor máximo al que pudo llegar es {}".format(num))