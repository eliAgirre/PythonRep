"""

Ejercicio 11

Pide al usuario dos números y muestra la “distancia” entre ellos 
(el valor absoluto de su diferencia, de modo que el resultado sea 
siempre positivo).

"""
try:
	num1 = float(input("Introduzca un número: "))
	num2 = float(input("Introduzca otro número: "))
	distancia = abs(num1 - num2)
	print("Distancia: ", distancia)
except ValueError:
	print("Introduza un número.")