#Ejercicio 6
año = int(input("Escriba un año: "))

if(año % 4 == 0):
  if(año % 100 == 0):
    if(año % 400 == 0):
      print("{} es bisiesto".format(año))
    else:
      print("{} no es bisiesto".format(año))
  else:
    print("{} es bisiesto".format(año))
else:
  print("{} no es bisiesto".format(año))