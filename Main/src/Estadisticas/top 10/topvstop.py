import os
import pandas as pd
from tabulate import tabulate
import json
import re

# Rutas de los archivos JSON
ruta_a = "/home/david/Documentos/pypokemtrics/Main/data/raw/json/paradox rift/Paradox rif 2023.json"
ruta_b = "/home/david/Documentos/pypokemtrics/Main/data/raw/json/paradox rift/paradox rift 2024.json"

# Ruta para guardar CSV
ruta_csv = "/home/david/Documentos/pypokemtrics/Main/data/processed/excel/Barras_agrupadas"

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
    "Special": ''
}

# Función para limpiar el nombre de la carta
def remove_words(text):
    for word in replace_dict.keys():
        text = re.sub(r'\b' + re.escape(word) + r'\b', '', text)  # Eliminar palabra completa
    return ' '.join(text.split()).strip()  # Limpiar espacios extra

# Función para cargar un archivo JSON
def cargar_json(ruta):
    try:
        with open(ruta, 'r') as f:
            return json.load(f)["cartas"]
    except FileNotFoundError:
        print(f"Error: El archivo {ruta} no fue encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta} no se pudo decodificar.")
        return []

# Función para extraer el top 10 de cartas de un mes en un archivo JSON
def extraer_top_10(json_data, mes):
    top_mes = {}
    for registro in json_data:
        if registro["mes"].lower() == mes.lower():
            for carta in registro["cartas"]:
                nombre_carta = remove_words(carta['nombre']) + f" - {carta['id_carta']}"
                top_mes[nombre_carta] = carta["precio"]
    
    # Obtener el top 10 de ese mes
    return dict(sorted(top_mes.items(), key=lambda x: x[1], reverse=True)[:10])

# Función para formatear el DataFrame combinado
def formatear_dataframe(df_combinado):
    if df_combinado.empty:
        print("El DataFrame está vacío, no se puede formatear.")
        return pd.DataFrame()  # Retorna un DataFrame vacío
    df_formateado = df_combinado.pivot(index='Nombre', columns=['Mes', 'Año'], values='Precio').fillna(0)
    return df_formateado

# Función para guardar el DataFrame formateado en un archivo CSV
def guardar_en_csv(df, nombre_archivo):
    ruta_completa = os.path.join(ruta_csv, nombre_archivo)
    df.to_csv(ruta_completa, index=True)  # Guarda con índice para conservar el nombre de la carta como fila
    print(f"DataFrame formateado guardado en {ruta_completa}")

# Cargar cada archivo JSON
json_data_a = cargar_json(ruta_a)
json_data_b = cargar_json(ruta_b)

# Especificar los meses que deseas extraer
mes_a = "December"  # Mes en el archivo A
mes_b = "January"  # Mes en el archivo B

# Extraer el top 10 de cada JSON para los meses especificados
top_10_a = extraer_top_10(json_data_a, mes_a)
top_10_b = extraer_top_10(json_data_b, mes_b)

# Convertir los diccionarios de top 10 en DataFrames, añadiendo columnas de mes y año
def crear_dataframe_top_10(diccionario_top, mes, año):
    df = pd.DataFrame(diccionario_top.items(), columns=['Nombre', 'Precio'])
    df['Mes'] = mes
    df['Año'] = año
    return df

# Crear DataFrames para los meses especificados
df_a = crear_dataframe_top_10(top_10_a, mes_a, 2023) if top_10_a else pd.DataFrame()
df_b = crear_dataframe_top_10(top_10_b, mes_b, 2024) if top_10_b else pd.DataFrame()

# Combinar ambos DataFrames en uno solo si ambos existen
dataframes = [df_a, df_b]
df_combinado = pd.concat(dataframes, ignore_index=True) if not df_a.empty and not df_b.empty else pd.DataFrame()

# Mostrar el DataFrame combinado
if not df_combinado.empty:
    print("\nDataFrame Combinado:")
    print(tabulate(df_combinado, headers='keys', tablefmt='grid'))

    # Formatear el DataFrame
    df_formateado = formatear_dataframe(df_combinado)

    # Mostrar el DataFrame formateado
    print("\nDataFrame Formateado para Gráfico de Barras Agrupado:")
    print(tabulate(df_formateado, headers='keys', tablefmt='grid'))

    # Guardar el DataFrame formateado en un archivo CSV
    nombre_archivo_csv = "Barras_agrupadas.csv"  # Nombre de archivo fijo o dinámico
    guardar_en_csv(df_formateado, nombre_archivo_csv)
else:
    print("No hay datos disponibles para los meses especificados.")
