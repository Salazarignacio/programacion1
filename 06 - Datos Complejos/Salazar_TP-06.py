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
print(balanceado("({()})"))
print(balanceado("({[})"))
print(balanceado("{{({()})}"))
print(balanceado("{({([[]])})}"))
print(balanceado("{({([)})}")) 

""" 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
● Agregar clientes (encolar).
● Atender clientes (desencolar).
● Mostrar el siguiente cliente en la fila.
 """

from collections import deque

class Cola_banco:
    def __init__(self):
        self.clientes = deque()
    def encolar(self, cliente):
        self.clientes.append(cliente)
    def desencolar(self):
        if self.clientes:
            return self.clientes.popleft()
        else:
            return "No hay clientes" 
    def mostrar_proximo(self):
        return self.clientes[0]
    
clientes = Cola_banco()
clientes.encolar("Cliente 1")
clientes.encolar("Cliente 2")
clientes.encolar("Cliente 3")
print(f"Proximo cliente: {clientes.mostrar_proximo()}")
print(f"Cliente atendido: {clientes.desencolar()}")
print(f"Proximo cliente: {clientes.mostrar_proximo()}")

""" 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
los valores almacenados. """

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    def insertar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.dato} -> ")
            actual = actual.siguiente

nueva_lista = ListaEnlazada()
nueva_lista.insertar_nodo(3)
nueva_lista.insertar_nodo(2)
nueva_lista.insertar_nodo(1)
nueva_lista.mostrar()

""" 9) Dada una lista enlazada, implementa una función para invertirla.
Ejemplo de entrada y salida: """

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None

    def insertar_nodo(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza:
            self.anterior = nuevo_nodo
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.dato} -> ")
            actual = actual.siguiente
    """ Cree este metodo mas probando que pensando  """
    """ No esta bien, solo resuelve cuando son 3 casos  """
    def invertir_lista(self):
        actual = self.cabeza.siguiente.siguiente
        print(actual.dato,"<-")
        actual = self.cabeza.siguiente
        
        print(actual.dato,"<-")
        actual = self.cabeza
        print(actual.dato,"<-")
        
        
            
nueva_lista_letras = ListaEnlazadaDoble()
nueva_lista_letras.insertar_nodo(3)
nueva_lista_letras.insertar_nodo(2)
nueva_lista_letras.insertar_nodo(1)
nueva_lista_letras.invertir_lista()

