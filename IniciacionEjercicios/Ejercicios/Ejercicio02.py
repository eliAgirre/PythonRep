# Ejercicio 2
# Calcular el perimetro y area de un rectangulo dada su base y su altura.

# base = anchura
# perimetro = 2 * (altura + anchura)
# area = base * altura

base = float(input("Introduzca la base del rectangulo: "))
altura = float(input("Introduzca la altura del rectangulo:"))
perimetro = 2 * (base + altura)
area = base + altura
print("El perimetro es: ", perimetro)
print("El area es: ", area)