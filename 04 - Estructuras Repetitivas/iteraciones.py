""" Desarrollar un algoritmo que permita ingresar una cantidad de personas. La computadora debe
pedir la edad de cada una y finalmente mostrar el porcentaje de personas que es mayor de edad """



mayores = 0.0
porcentaje = 0
personas = 6

for cont in range(personas):
    edadPersona = int(input("Ingrese su edad"))
    if edadPersona > 17:
        mayores += 1
porcentaje = 100 / personas * mayores
print(porcentaje)
