import pandas as pd
import os
from tabulate import tabulate
import json

# Ruta al archivo JSON
ruta_json = "/home/david/Documentos/pypokemtrics/Main/data/raw/json/paradox rift/paradox rift 2024.json"
# Ruta base donde se guardará el archivo CSV
ruta_base_csv = "/home/david/Documentos/pypokemtrics/Main/data/processed/excel/grafico lineal"

def buscar_precio_por_id(json_data, carta_id):
    """
    Busca el precio de una carta por su ID en los datos JSON proporcionados.

    Args:
        json_data (dict): Los datos JSON que contienen información sobre las cartas.
        carta_id (str): El ID de la carta cuyo precio se desea buscar.

    Returns:
        pd.DataFrame: Un DataFrame que contiene los meses y los precios de la carta.
                      Si no se encuentra la carta, devuelve None.
    """
    
    # Diccionario para almacenar los precios por mes
    precios_por_mes = {}

    # Recorrer cada expansión por mes
    for expansion in json_data["cartas"]:
        mes = expansion["mes"]
        
        # Buscar la carta dentro del mes
        for carta in expansion["cartas"]:
            if carta["id_carta"] == carta_id:
                # Añadir el precio de la carta en ese mes
                precios_por_mes[mes] = carta["precio"]
    
    # Verificar si se encontraron precios
    if not precios_por_mes:
        print("ID de carta no encontrado")
        return None

    # Ordenar los meses cronológicamente (sin el año)
    meses_ordenados = sorted(precios_por_mes.keys(), key=lambda x: pd.to_datetime(x, format="%B"))
    precios_ordenados = [precios_por_mes[mes] for mes in meses_ordenados]

    # Crear un DataFrame con los datos de los meses y precios
    df = pd.DataFrame({
        'Mes': meses_ordenados,
        'Precio': precios_ordenados
    })
    
    return df

def guardar_csv(df):
    """
    Guarda el DataFrame en un archivo CSV.

    Args:
        df (pd.DataFrame): El DataFrame a guardar.

    Returns:
        None
    """
    nombre_archivo = input("Introduce el nombre del archivo CSV (sin extensión): ")
    ruta_csv = os.path.join(ruta_base_csv, f"{nombre_archivo}.csv")
    try:
        df.to_csv(ruta_csv, index=False)
        print(f"DataFrame guardado exitosamente en: {ruta_csv}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# Cargar el JSON desde el archivo
with open(ruta_json, 'r') as f:
    json_data = json.load(f)

# Buscar precios y mostrar en formato tabulado
df = buscar_precio_por_id(json_data, "199/182")
if df is not None:
    print(tabulate(df, headers='keys', tablefmt='pretty'))

# Llamar a la función para guardar el DataFrame en CSV
guardar_csv(df)

# Comentado porque no deseas ver los tipos de columnas
# tipos_columnas = tipos_de_datos(df)
# print(tipos_columnas)
