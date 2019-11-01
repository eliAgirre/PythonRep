"""

Ejercicio 12

Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos 
en el plano. Calcula y muestra la distancia entre ellos.

"""
import math

print("Introduzca un punto de coordenada: ")
x1 = float(input("Introduzca el punto x1: "))
y1 = float(input("Introduzca el punto y1: "))

print("Introduzca otro punto de coordenada: ")
x2 = float(input("Introduzca el punto x2: "))
y2 = float(input("Introduzca el punto y2: "))

distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print("Distancia: ", distancia)


"""

De otra forma:

import math

print("Introduzca un punto de coordenada: ")
x1 = float(input("Introduzca el punto x1: "))
y1 = float(input("Introduzca el punto y1: "))

print("Introduzca otro punto de coordenada: ")
x2 = float(input("Introduzca el punto x2: "))
y2 = float(input("Introduzca el punto y2: "))

distancia = math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2))
print("Distancia: ", distancia)

"""