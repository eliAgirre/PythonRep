"""
Ejercicio 8

Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
las tres ventas que realiza en el mes y el total que recibirá en el mes 
tomando en cuenta su sueldo base y comisiones. """

# sueldoBase + 10% extra por comision
# 3 ventas
# comisiones al mes y el total
try:
	sueldoBase = float(input("Introduza el sueldo base: "))
	venta1 = float(input("Introduza la venta 1: "))
	venta2 = float(input("Introduza la venta 2: "))
	venta3 = float(input("Introduza la venta 3: "))
	comision = (venta1 * 0.1) + (venta2 * 0.1) + (venta3 * 0.1)
	print("Comisión del mes: ", comision)
	print("Comisión total: ", sueldoBase + comision)
except ValueError:
	print("Introduza números en el sueldo base y en las ventas.")
	print("Comisión del mes: 0.0")
	print("Comisión total: 0.0")