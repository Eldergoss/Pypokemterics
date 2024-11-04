import json
import pandas as pd
from tabulate import tabulate
import re

# Cargar el JSON desde el archivo (ajusta la ruta según sea necesario)
ruta_json = "/home/david/Documentos/pypokemtrics/Main/data/raw/json/paradox rift/paradox rift 2024.json"
with open(ruta_json, 'r') as f:
    json_data = json.load(f)

# Diccionario para eliminar palabras específicas
replace_dict = {
    'Sketch': '',
    'Rare': '',
    'Trainer': '',
    'Supporter': '',
    'Full': '',
    'Art': '',
    'Hyper': '',
    'Illustration': '',
    "Special" : " "
}

# Función para limpiar el nombre de la carta
def remove_words(text):
    for word in replace_dict.keys():
        text = re.sub(r'\b' + re.escape(word) + r'\b', '', text)  # Eliminar palabra completa
    text = ' '.join(text.split())  # Limpiar espacios extra
    return text.strip()  # Eliminar espacios al inicio y final

def top(mes):
    top_ten = {}

    for registro in json_data["cartas"]:
        if registro["mes"].lower() == mes.lower():
            for carta in registro["cartas"]:
                nombre_carta = remove_words(carta['nombre'])  # Limpiar el nombre de la carta
                nombre_carta += f" - {carta['id_carta']}"  # Concatenar ID
                top_ten[nombre_carta] = carta["precio"]

    top_ten = dict(sorted(top_ten.items(), key=lambda x: x[1], reverse=True)[:10])
    return top_ten

def guardar_csv(dataframe):
    respuesta = input("¿Deseas guardar los datos como un archivo CSV? (s/n): ").strip().lower()
    if respuesta == 's':
        nombre_archivo = input("Ingresa el nombre del archivo CSV (sin extensión): ").strip()
        ruta_csv = f'{nombre_archivo}.csv'
        dataframe.to_csv(ruta_csv, index=False)
        print(f"Datos guardados en: {ruta_csv}")
    else:
        print("No se guardaron los datos.")

# Llamada a la función con el mes en formato de texto
top_cartas = top("October")

# Convertir el diccionario a DataFrame y mostrarlo
data = pd.DataFrame(top_cartas.items(), columns=['Nombre', 'Precio'])
print(tabulate(data, headers='keys', tablefmt='pretty', showindex=False))

# Preguntar si se desea guardar el DataFrame como CSV
guardar_csv(data)
