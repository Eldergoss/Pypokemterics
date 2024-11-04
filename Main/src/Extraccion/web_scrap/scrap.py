import requests
import os
from bs4 import BeautifulSoup


# Función de extracción de título
def extrac_tittle(iterable):  # recibimos un iterable como argumento de la función
    # Realizamos la solicitud HTTP
    response = requests.get(iterable)  # usamos el argumento 'iterable'
    html = response.text
    
    # Parseamos el HTML con BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Comienza la extracción del título (ejemplo: usando la etiqueta 'h1')
    titulo = soup.find("h1", class_="headline")
    
    # Devolvemos el texto del título si existe, de lo contrario devolvemos None
    return titulo.text if titulo else "Título no encontrado"

""" Llamada a la función con un URL
url = "https://bleedingcool.com/games/pokemon-tcg-value-watch-obsidian-flames-in-august-2024/"
a = extrac_tittle(url).split()
print(a)"""

#funcion que extrae el top 10 de cartas


def extract_top10(iterable):
    # Realiza la solicitud HTTP al URL proporcionado en 'iterable'
    response = requests.get(iterable)
    xtml = response.text  # Obtiene el contenido HTML de la respuesta
    
    # Parseamos el HTML utilizando BeautifulSoup
    soup = BeautifulSoup(xtml, 'html.parser')
    
    # Encontramos todos los elementos <ol> en el HTML
    listas_ol = soup.find_all("ol")
    
    # Verificamos si hay al menos 3 listas <ol>
    if len(listas_ol) >= 3:
        # Seleccionamos el segundo elemento <ol> (el índice es 1)
        listas_ol = listas_ol[1]
        
        # Buscamos todos los elementos de la lista <li> dentro del segundo <ol>
        items = listas_ol.find_all("li")
        
        # Extraemos el texto de los primeros 10 elementos <li>
        top_items = [item.get_text(strip=True) for item in items[:10]]
        
        # Devolvemos la lista de los 10 elementos extraídos
        return top_items  

    # Si no hay suficientes elementos <ol>, devolvemos una lista vacía
    return []  

        
"""        
b = extract_top10(url)
print(b)
"""







