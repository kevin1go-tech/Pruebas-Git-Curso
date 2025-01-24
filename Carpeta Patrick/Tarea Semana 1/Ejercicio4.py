#Ejercicio 4
numero1 = int(input("Escriba el primer número: "))
numero2 = int(input("Escriba el segundo número: "))
if (numero1 > numero2):
  residuo = numero1 % numero2
  if (residuo == 0):
    print("{} es multiplo de {}".format(numero1, numero2))
  else:
    print("{} no es multiplo de {}".format(numero1, numero2))
else:
  residuo = numero2 % numero1
  if (residuo == 0):
    print("{} es multiplo de {}".format(numero2, numero1))
  else:
    print("{} no es multiplo de {}".format(numero2, numero1))