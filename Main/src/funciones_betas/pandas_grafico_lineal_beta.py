import pandas as pd
import os
from tabulate import tabulate
import json

# Ruta al archivo JSON
ruta_json = "/home/david/Documentos/pypokemtrics/Main/data/raw/json/paradox rift/paradox rift 2024.json"

def buscar_precio_por_id(json_data, carta_id):
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

    # Calcular la diferencia de precio entre meses
    #df['Diferencia de Precio'] = df['Precio'].shift(1) - df['Precio']
    # Calcular la diferencia de precio entre meses
    df['Diferencia de Precio'] = df['Precio'] - df['Precio'].shift(1)


    # Redondear la columna de diferencia de precio a dos decimales
    df['Diferencia de Precio'] = df['Diferencia de Precio'].round(2)
    
    return df

# Cargar el JSON desde el archivo
with open(ruta_json, 'r') as f:
    json_data = json.load(f)

# Buscar precios y mostrar en formato tabulado
df = buscar_precio_por_id(json_data, "199/182")
if df is not None:
    print(tabulate(df, headers='keys', tablefmt='pretty'))
import pandas as pd

def tipos_de_datos(df):
    """
    Devuelve el tipo de dato de cada columna en el DataFrame.

    Args:
    df (pd.DataFrame): El DataFrame a analizar.

    Returns:
    dict: Un diccionario con el nombre de cada columna y su tipo de dato.
    """
    tipos = {}
    for columna in df.columns:
        tipos[columna] = df[columna].dtype
    return tipos

# Ejemplo de uso
# Supongamos que tienes un DataFrame df ya definido
tipos_columnas = tipos_de_datos(df)
print(tipos_columnas)
