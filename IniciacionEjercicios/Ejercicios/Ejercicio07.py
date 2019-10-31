""" Ejercicio 7

Realiza un programa que reciba una cantidad de minutos y 
muestre por pantalla a cuantas hora y minutos corresponde.
Por ejemplo: 1000 minutos son 16 horas y 40 minutos. """

# 1 minuto es igual a 0,06 horas. O 1 hora son 60 minutos.

"""
minutos = float(input("Introduce la cantidad de minutos:"))
horas = minutos / 60
parteEnteraHoras = int(horas)
mins = horas - parteEnteraHoras
minsMostrar = int(mins * 60)
print("Horas: ", parteEnteraHoras, " Minutos: ", minsMostrar)
"""

# Se puede hacer mas reducido:
try:
	minutos = int(input("Introduce la cantidad de minutos:"))
	res_horas = minutos // 60
	res_min = minutos % 60
	print(res_horas,"horas y",res_min,"minutos.")
except ValueError:
	print("Introduza un número")
	print("0 horas y 0 minutos.")