""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal. """
def imprimir_hola_mundo():
    print("Hola mundo")

imprimir_hola_mundo()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario. """

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre) 

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados. """

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = input("Por favor ingrese su edad: ")
residencia = input("Por favor ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados."""

def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    print(f"El area del circulo es {area}")
def calcular_perimetro(radio):
    perimetro = 2 * 3.14 * radio
    print(f"El perimetro del circulo es {perimetro}")

radio = int(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro(radio)

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función."""

def segundos_a_horas(segundos):
    print(f"Corresponde a {segundos / 60 / 60} horas")

segundos = int(input("Por favor ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

def tabla_multiplicar(numero):
    for i in range(11):
        print(f"{i} x {numero} = {i * numero}")

def validar_numero():
    num = int(input("Ingrese un numero entero del 1 al 10: "))
    while num <= 0 or num > 10:
        num = int(input("ERROR, Ingrese un numero entero del 1 al 10: "))
    return num

num = validar_numero()
tabla_multiplicar(num)

"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
de forma clara."""

def operaciones_basicas(a, b):
    print(f"Sumados: {a + b}, Restados: {a - b}, Multiplicados: {a * b}, Divididos: {a/b}")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

operaciones_basicas(num1, num2)

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales. """

def calcular_imc(peso, altura):
    print(f"Su IMC es de {peso / altura ** 2}")

peso = float(input("Por favor ingrese su peso en kgs: "))
altura = float(input("Por favor ingrese su altura: "))

calcular_imc(peso, altura)

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función. """

def celsius_a_farenheit(celsius):
    print(f"Equivalen a {9/5*celsius + 32} grados farenheit")

celsius = float(input("Por favor ingrese la temperatura en celsius: "))
celsius_a_farenheit(celsius)

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función. """

def calcular_promedio(a, b, c):
    print(f"El promedio es {(a + b + c)/3}")

n1 = int(input("Por favor ingrese el primer numero: "))
n2 = int(input("Por favor ingrese el segundo numero: "))
n3 = int(input("Por favor ingrese el tercer numero: "))

calcular_promedio(n1, n2, n3)