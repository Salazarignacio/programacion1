
""" 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300 """

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800 """

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800
print(precios_frutas)

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios. """

lista_precios_frutas = list(precios_frutas.keys())
print(lista_precios_frutas)

""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
 """

class Agenda:
    def __init__(self):
        self.contactos = {}
    def agendar(self, nombre, nro):
        self.contactos[nombre] = nro
    def mostrar(self, nombre):
        if nombre in self.contactos:
            print(f"El numero de {nombre} es {self.contactos[nombre]}")
        else:
            print(f"{nombre} no se encuentra en su agenda")

agenda = Agenda()

nombre = input("Ingrese el nombre del contacto: ")
numero = input("Ingrese el numero del contacto: ") 
contador = 1
while contador < 6:
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero del contacto: ")
    contador += 1

agenda.agendar(nombre, numero)
nombre = input("Ingrese el nombre del contacto que desea buscar en su agenda: ")
agenda.mostrar(nombre) 

"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra  """

frase = input("Ingrese una frase")
frase = frase.split()
set_palabras = set(frase)

diccionario_frase = {}

for i in range(len(frase)):
    if frase[i] in diccionario_frase:
        diccionario_frase[frase[i]] += 1
    else:
        diccionario_frase[frase[i]] = 1

print(f"Palabras unicas: {set_palabras}")
print(f"Aparecicion de cada palabra {diccionario_frase}") 

""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno. """

alumno1 = input("Ingrese nombre alumno 1")
alumno2 = input("Ingrese nombre alumno 2")
alumno3 = input("Ingrese nombre alumno 3") 
alumno1 = (alumno1, 10, 9, 8)
alumno2 = (alumno2, 7, 7, 3)
alumno3 = (alumno3, 4, 9, 2)

array_alumnos = [alumno1, alumno2, alumno3]
for i in range(len(array_alumnos)):
    print(f"el promedio de {array_alumnos[i][0]} es {(array_alumnos[i][1] + array_alumnos[i][2] + array_alumnos[i][3]) / 3}" )

""" 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """

set1 = {"Angel", "Marco", "Carlos", "Facundo", "Enzo"}
set2 = {"Angel", "Alejo", "Ariel", "Agustin", "Emiliano"}

print(f"Aprobaron ambos examenes: {set1 & set2}")
print(f"Aprobaron un solo examen: {set1 ^ set2}")
print(f"Aprobaron al menos un examen: {set1 | set2}")

""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe. """

class Stock:
    def __init__(self):
        self.productos = {}
    def agregar_producto(self,producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
    def consultar_stock(self, producto):
        print(f"Hay {self.productos[producto]} de {producto} ")

stock = Stock()
stock.agregar_producto("tomate", 3)
stock.agregar_producto("zanahoria", 8)
stock.agregar_producto("zanahoria", 3)
stock.consultar_stock("zanahoria")

""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Ejemplo: """
""" Permití consultar qué actividad hay en cierto día y hora. """

class Agenda():
    def __init__(self):
        self.actividades = {}
    def agregar_actividad(self, dia, hora, actividad):
        self.actividades[(dia, hora)] = actividad
    def consultar_actividad(self, dia, hora):
        if (dia, hora) in self.actividades:
            print(f"Tienes {self.actividades[(dia, hora)]}")
        else:
            print("tiene agenda libre")
    def mostrar_actividad(self):
        print(self.actividades)

agenda = Agenda()
agenda.agregar_actividad("lunes", "14:40", "Ingles")
agenda.agregar_actividad("martes", "13:10", "Dentista")
agenda.mostrar_actividad()
agenda.consultar_actividad("lunes", "14:40")


""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores """

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "Paris",
    "Alemania": "Berlin",
    "Japon": "Tokio"
}

capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario invertido (capital > pais):")
print(capitales)