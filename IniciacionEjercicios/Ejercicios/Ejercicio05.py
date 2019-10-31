""" Ejercicio 5

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Recordar que la formula para la conversion es:

C = (F - 32) * 5/9
"""

fahrenheit = float(input("Introduzca los grados de fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Grados Celsius: ", celsius)