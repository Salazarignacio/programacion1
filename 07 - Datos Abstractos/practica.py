
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