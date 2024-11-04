import os
import requests
from bs4 import BeautifulSoup

items = None
# URL de ejemplo (cambia por la URL que desees analizar)
url = "https://bleedingcool.com/games/pokemon-tcg-value-watch-paradox-rift-in-january-2024/"
#'https://bleedingcool.com/games/pokemon-tcg-value-watch-fusion-strike-in-august-2024/'
#'https://bleedingcool.com/games/pokemon-tcg-value-watch-lost-origin-in-august-2024/'
#"https://bleedingcool.com/games/pokemon-tcg-value-watch-obsidian-flames-in-august-2024/"
#'https://bleedingcool.com/games/pokemon-tcg-value-watch-paldea-evolved-in-june-2024/'

# Realizamos la solicitud HTTP
response = requests.get(url)
html = response.text

# Parseamos el HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontramos todos los elementos <ol> en el HTML
listas_ol = soup.find_all('ol')

# Verificamos que exista al menos un tercer elemento <ol>
if len(listas_ol) >= 3:
    # Seleccionamos el tercer elemento <ol> (índice 2 en Python, empezando desde 0)
    lista_ol = listas_ol[1]  # Usamos el índice 2 para el tercer elemento

    # Encontramos todos los elementos <li> dentro de la lista <ol>
    items = lista_ol.find_all('li')

    if items:  # Verificamos si `items` no está vacío
        # Nombre del archivo de salida
        archivos_txt = 'resultado.txt2'
        ruta = "/home/david/python_project/Graficas_beta/data_raw/"
        
        # Ruta completa del archivo
        ruta_completa = os.path.join(ruta, archivos_txt)


        # Abrir el archivo en modo escritura ('w')
# Iteramos sobre los primeros diez elementos de `items`. Aunque `items` es un ResultSet, se comporta de manera similar a una lista,
# por lo que podemos usar el slicing `[:10]` para obtener los primeros diez elementos.
        with open(ruta_completa, 'w', encoding='utf-8') as t:
            for item in items[:5]:
                text = item.get_text(strip=True)
                t.write(text + '\n')  # Escribir cada línea seguida de un salto de línea
    
else:
    print("No se encontró un tercer elemento <ol> en el HTML.")
