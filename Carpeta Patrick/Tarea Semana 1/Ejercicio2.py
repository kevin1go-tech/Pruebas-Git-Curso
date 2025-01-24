#Ejercicio 2
import math
cateto1 = int(input("Ingresa el valor del cateto a: "))
cateto2 = int(input("Ingresa el valor del cateto b: "))
print("-------------------------------------------")
print("La formula para hallar esto es a^2 + b^2 = c^2")
print("Donde c^2 es el valor de la hipootenusa, y a,b el de los catetos")
hipotenusa = math.sqrt((cateto1**2)+(cateto2**2))
print("-------------------------------------------")
print("La hipotenusa es igual a: ", hipotenusa)