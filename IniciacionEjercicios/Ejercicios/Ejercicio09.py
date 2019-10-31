"""

Ejercicio 9

Una tienda ofrece un descuento del 15% sobre el total de la compra y 
un cliente desea saber cuanto deberá pagar finalmente por su compra.

"""

# descuento -> 15% de la compra total

try:
	compraTotal = float(input("Introduza el importe de la compra total: "))
	aPagar = compraTotal - (compraTotal * 0.15)
	print("A pagar: ", aPagar)
except ValueError:
	print("Introduza un número en la compra total.")
	print("A pagar 0.0€ €")