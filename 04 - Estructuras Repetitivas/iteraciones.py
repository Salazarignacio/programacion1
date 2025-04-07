"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """

num = float(input("Por favor ingrese un numero "))
copia_num = num
numero_final = 0
cifras = 1
cifras_2 = 1

while num >= 1: 
    while copia_num > 9:
        copia_num /= 10
        cifras *= 10 
        copia_num = int(copia_num)
        """ numero_final = copia_num """
    numero_final = numero_final + copia_num * cifras_2
    num = num - (copia_num * cifras)
    copia_num = num
    cifras = 1
    cifras_2 *=10
    
print(f"El numero al reves es {numero_final}")

""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""
for cont in range(101):
    """ print(cont) """

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""
numero = int(input("Por favor ingrese un numero entero"))
digitos = 1
while numero / 10 >= 1:
    numero /= 10
    digitos += 1
print(f"el numero {numero} tiene {digitos} digitos")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""
num1 = int(input("Introduzca el primer valor"))
num2 = int(input("Introduzca el segundo valor"))
acumulador = 0

for cont in range(num1,num2+1):
    acumulador += cont
print(f"La suma de los numeros comprendidos entre {num1} y {num2} es {acumulador}")

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

num1 = int(input("Introduzca un numero entero "))
num2 = int(input("Introduzca otro numero entero "))
acumulado = 0
while num1 != 0 and num2 != 0:
    acumulado += num1 + num2
    num1 = int(input("Introduzca un numero entero "))
    num2 = int(input("Introduzca otro numero entero "))
print(f"El numero acumulado es {acumulado}")

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
import random

intentos = 0
num = int(input("Por favor introduzca un numero del 0 al 9 "))
aleatorio = random.randint(0, 9)
while num != aleatorio:
    num = int(input(f"No has adivinado. Introduzca otro numero "))

if num == aleatorio:
    print(f"Has adivinado! El numero es {aleatorio}")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

for cont in range(100, 0, -2):
    print(cont)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

num = int(input("Por favor introduzca un numero positivo"))
acumulador = 0

for cont in range(0,num +1): 
    """Deduje que el numero dado tambien se suma"""
    acumulador += cont

print(f"El numero acumulado es {acumulador}")

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

pares = 0
impares = 0
positivos = 0 
negativos = 0

for cont in range(100):
    num = int(input("Por favor ingrese un numero"))
    if num != 0:
        if num % 2 == 0:
            pares += 1
        else:
            impares +=1
        if num > 0:
            positivos += 1
        else: 
            negativos += 1

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

acumulador = 0
rango = 5

for cont in range(rango):
    num = int(input("Ingrese un numero "))
    acumulador += num
media = acumulador / rango

print(f"La media de todos los numeros ingresados es {media}")