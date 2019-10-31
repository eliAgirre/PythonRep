""" Ejercicio 4
Dado dos numeros, mostrar la suma, resta, division y multiplicacion de ambos """

try:
	numero1 = float(input("Introduce el numero 1: "))
	numero2 = float(input("Introduce el numero 2: "))
	suma = numero1 + numero2
	resta = numero1 - numero2
	division = numero1 / numero2
	multiplicacion = numero1 * numero2
	print("Suma: ", suma, "Resta: ", resta, "Division: ", division, "multiplicacion: ", multiplicacion)
except ZeroDivisionError:
	print("No introduzca un cero, no se puede dividir")
	multiplicacion = numero1 * numero2
	print("Suma: ", suma, "Resta: ", resta, "Division: 0.0", "multiplicacion: ", multiplicacion)	