"""

Ejercicio 10

Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

    55% del promedio de sus tres calificaciones parciales.

    30% de la calificación del examen final.

    15% de la calificación de un trabajo final.

"""

try:
	parcial1 = float(input("Introduzca la calificación del parcial 1: "))
	parcial2 = float(input("Introduzca la calificación del parcial 2: "))
	parcial3 = float(input("Introduzca la calificación del parcial 3: "))
	examen = float(input("Introduzca la calificación del examen: "))
	trabajo = float(input("Introduzca la calificación del trabajo: "))
	promedio = ((parcial1 + parcial2 + parcial3)/3) * 0.55
	nota = promedio + (examen * 0.30) + (trabajo * 0.15)
	#print("Promedio: ", promedio, "Examen final: ", examen * 0.30, "Trabajo final: ", trabajo * 0.15)
	print("Nota: ", nota)
except ValueError:
	print("Introduza un número en las calificaciones.")
