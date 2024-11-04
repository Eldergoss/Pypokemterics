import os
import pandas as pd
from tabulate import tabulate
import json

# Ruta al archivo JSON
ruta_json = "/home/david/Documentos/pypokemtrics/Main/data/raw/json/paradox rift/paradox rift 2024.json"
# Ruta para guardar el archivo CSV
ruta_csv = "/home/david/Documentos/pypokemtrics/Main/data/processed/excel"

def buscar_precios_por_ids(json_data, carta_id1, carta_id2):
    # Diccionarios para almacenar los precios de cada carta por mes
    precios_carta1 = {}
    precios_carta2 = {}

    # Recorrer cada mes en la expansión
    for mes_data in json_data["cartas"]:
        mes = mes_data["mes"]
        año = mes_data["año"]
        fecha = f"{mes}-{año}"

        # Buscar las cartas dentro de cada mes
        for carta in mes_data["cartas"]:
            if carta["id_carta"] == carta_id1:
                precios_carta1[fecha] = carta["precio"]
            elif carta["id_carta"] == carta_id2:
                precios_carta2[fecha] = carta["precio"]

    return precios_carta1, precios_carta2

# Leer archivo JSON
with open(ruta_json, "r") as archivo_json:
    datos_json = json.load(archivo_json)

# Ejemplo de uso de la función
id_carta1 = "249/182"  # Reemplazar con el ID de la primera carta
id_carta2 = "199/182"  # Reemplazar con el ID de la segunda carta
precios_carta1, precios_carta2 = buscar_precios_por_ids(datos_json, id_carta1, id_carta2)

# Crear DataFrame combinando los datos de ambas cartas
df_precios = pd.DataFrame({
    "Mes": list(precios_carta1.keys()),
    "Precio Carta 1": list(precios_carta1.values()),
    "Precio Carta 2": list(precios_carta2.values())
})

# Mostrar tabla con el formato de salida solicitado
print(tabulate(df_precios, headers=["Mes", "Precio Carta 1", "Precio Carta 2"], tablefmt="grid"))

# Preguntar si se quiere guardar como CSV
guardar_csv = input("¿Quieres guardar los datos como archivo CSV? (s/n): ")
if guardar_csv.lower() == 's':
    nombre_archivo = input("Introduce el nombre del archivo (sin extensión): ")
    ruta_completa = os.path.join(ruta_csv, f"{nombre_archivo}.csv")
    
    # Guardar DataFrame en CSV
    df_precios.to_csv(ruta_completa, index=False)
    print(f"Archivo guardado como: {ruta_completa}")
