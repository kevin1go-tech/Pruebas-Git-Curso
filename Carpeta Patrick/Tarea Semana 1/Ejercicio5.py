#Ejercicio 5
numero1 = int(input("Escriba el primer número: "))
numero2 = int(input("Escriba el segundo número: "))

if (numero1 > 0) and (numero2 > 0):
  if (numero1 > numero2):
    residuo = numero1 % numero2
    mayor, menor = numero1, numero2
  else:
    residuo = numero2 % numero1
    mayor, menor = numero2, numero1

  if (residuo == 0):
    print("{} es multiplo de {}".format(mayor, menor))
  else:
    print("{} no es multiplo de {}".format(mayor, menor))
else:
  print("Su número es cero o negativo, por favor, vuelva a ingresar")

