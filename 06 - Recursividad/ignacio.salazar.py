""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
y devuelva su representación en binario como una cadena de texto. """

def decimal_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    elif num % 2 == 0:
        str_numero = decimal_binario(num // 2)
        str_numero += "0" + str_numero
        return str_numero
    else:
        str_numero = decimal_binario(num // 2)
        str_numero +=  "1" + str_numero 
        return str_numero

def decimal_binario2(num):
    
    if num < 2:
        return str(num % 2)
    else:
        fact = decimal_binario2(num // 2) + str(num %2)
        return fact

print(decimal_binario2(29))

""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario """

def calcular_factorial(num):
    if num == 0:
        return 1
    else:
        return num * calcular_factorial(num-1)
    
numero = int(input("Ingrese un numero entero positivo para calcular su factorial: "))
print(f"El factorial de {numero} es {calcular_factorial(numero)}")
""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique. """

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
posicion = int(input("Ingrese un la posicion de fibonacci deseada: "))
print(f"La posicion {posicion} en sistema fibonacci equivale al numero {fibonacci(posicion)}")

""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general. """

def potenciar_numero(n, m):
    if m == 1:
        return n
    else:
        return n * potenciar_numero(n,m-1)

base = int(input("Ingrese el valor base que desea potenciar: "))
potencia = int(input("Ingrese el valor de la potencia: "))
print(f"{potenciar_numero(base,potencia)}")