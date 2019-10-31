# Ejercicio 3
# Dados los catetos de un triángulo rectangulo, calcular su hipotenusa

# hipotenusa = raiz cuadrada de la suma de los catetos de cada potencia

import math

"""cateto1 = float(input("Introduzca el cateto 1: "))
cateto2 = float(input("Introduzca el cateto 2: "))
hipotenusa = math.sqrt(pow(cateto1,2)+pow(cateto2,2))
print("Hipotenusa es: ", hipotenusa) """


# lo mismo pero sin pow

cateto1 = float(input("Introduzca el cateto 1: "))
cateto2 = float(input("Introduzca el cateto 2: "))
hipotenusa = math.sqrt(cateto1**2+cateto2**2)
print("Hipotenusa es: ", hipotenusa)