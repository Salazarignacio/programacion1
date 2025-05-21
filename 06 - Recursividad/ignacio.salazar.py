""" 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y
un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0 """

def contar_digito(numero, digito):
    if numero < 9:
        if numero == digito:
            return [1, numero]
        else:
            return [0, numero]
    else:
        return contar_digito(numero//10, digito) 

print(contar_digito(2122334212, 2))
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

""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
y devuelva su representación en binario como una cadena de texto. """

def decimal_binario2(num):
    if num < 2:
        return str(num % 2)
    else:
        fact = decimal_binario2(num // 2) + str(num %2)
        return fact

print(decimal_binario2(29))

""" 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed(). """

def es_palindromo(string):
    
    if len(string) == 1:
        return True
    elif len(string) == 2:
        return string[0] == string[-1:]
    else:
        return es_palindromo(string[1:-1])

print(es_palindromo("menem"))

""" 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y
devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5) """

def suma_digitos(num):
    if num <= 9:
        return num
    else:
        return suma_digitos(num // 10) + (num - num // 10 * 10)

print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(305))

""" 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel 
uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total 
de bloques que necesita para construir toda la pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1) """

def contar_bloques(n):
    if n == 1:
        return n
    else:
        return contar_bloques(n-1) + n
    
print(contar_bloques(1))
print(contar_bloques(2))
print(contar_bloques(4))