""" 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
balanceados usando una pila. """

def balanceado(string):
    pila = list(string)
    
    booleano = True
    largo = len(pila)
    """ Si tiene elementos impares no pueden estar emparejados, por tanto no estan correctamente balanceados """
    if largo % 2 != 0:
        booleano = False
    
    largo = int(largo/2)
    """ Se me ocurrio hacer un bucle que compare la primera mitad de la pila con el correspondiente en cada iteracion """
    """ A medida que el bucle avanza compara si el elemento recorrido esta siendo balanceado """
    """ En cada iteracion se elimina el ultimo elemento de la pila """
    for i in range(largo):
         if (pila[i] == "(" and pila[len(pila)-1] != ")") or (pila[i] == "{" and pila[len(pila)-1] != "}") or (pila[i] == "[" and pila[len(pila)-1] != "]"):
             return False
         else:
             pila.pop()
    return booleano

""" Se realizan varias pruebas para garantizar los resultados """
print(balanceado("{{({()})}"))
print(balanceado("({()})"))
print(balanceado("{({([[]])})}"))
print(balanceado("{({([)})}")) 

""" 1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
Añadir las siguientes frutas con sus respectivos precios: ● Naranja = 1200 ● Manzana = 1500 ● Pera = 2300 """

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naraja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: ● Banana = 1330 ● Manzana = 1700 ● Melón = 2800 """

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. """

lista_frutas = list(precios_frutas.keys())

""" 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años." """

class Persona:
    def __init__(self,nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    def saludar(self):
        print(f"Hola soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años")

persona = Persona("Ignacio", "Argentina", 38)
persona.saludar()

"""5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente. """
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return round(math.pi * self.radio ** 2)
    def calcular_perimetro(self):
        return round(math.pi * self.radio * 2)
    
circulo1 = Circulo(12)    
print(circulo1.calcular_area())
print(circulo1.calcular_perimetro())
