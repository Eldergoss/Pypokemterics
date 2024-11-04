import json
import os
import pandas as pd
from tabulate import tabulate  # Importar correctamente tabulate

# Ruta del archivo JSON
ruta_json = "/home/david/Documentos/pypokemtrics/Main/data/raw/json/paradox rift/paradox rift 2024.json"
# Ruta del archivo CSV
ruta_csv = "/home/david/Documentos/pypokemtrics/Main/data/processed/excel/tabla analitica"

# Cargar JSON
with open(ruta_json, "r") as f:
    data = json.load(f)

def prueba(data_json, id):
    precio_por_mes = {}

    # Ciclo for
    for expansion in data_json["cartas"]:
        mes = expansion["mes"]

        for carta in expansion["cartas"]:
            if carta["id_carta"] == id:
                precio_por_mes[f"{mes}"] = carta["precio"]

    if not precio_por_mes:
        print("ID de carta no encontrada")
        return None
        
    return precio_por_mes  # Retornar el diccionario correcto

# Llamar a la función
a = prueba(data, "199/182")

# Crear DataFrame
df = pd.DataFrame(list(a.items()), columns=["fecha", "precio"])

# Imprimir el DataFrame usando tabulate
print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))

def analizar_precios(df):
    """
    Analiza los precios mensuales y calcula el cambio porcentual, promedio acumulado y diferencia de precio.
    
    Args:
    df (pd.DataFrame): DataFrame que contiene las columnas 'fecha' y 'precio'.
    """
    
    # Calcular el cambio porcentual
    df["Cambio Porcentual"] = df["precio"].pct_change() * 100
    
    # Rellenar el primer mes con 0 (modificado para evitar FutureWarning)
    df["Cambio Porcentual"] = df["Cambio Porcentual"].fillna(0)

    # Calcular el promedio acumulado de cambio porcentual
    df["Promedio Acumulado"] = df["Cambio Porcentual"].expanding().mean()

    # Calcular la diferencia de precio entre el mes anterior y el mes actual
    df["Diferencia Precio"] = df["precio"] - df["precio"].shift(1)
    df["Diferencia Precio"] = df["Diferencia Precio"].fillna(0)  # Rellenar la primera diferencia con 0

    # Redondear a dos decimales
    df["precio"] = df["precio"].round(2)
    df["Cambio Porcentual"] = df["Cambio Porcentual"].round(2)
    df["Promedio Acumulado"] = df["Promedio Acumulado"].round(2)
    df["Diferencia Precio"] = df["Diferencia Precio"].round(2)

    # Calcular el total de precios
    total_precio = df["precio"].sum()
    total_cambio_porcentual = df["Cambio Porcentual"].sum()
    total_promedio_acumulado = df["Promedio Acumulado"].mean()
    total_diferencia_precio = df["Diferencia Precio"].sum()

    # Agregar una fila de totales
    totales = pd.DataFrame({
        "fecha": ["Total"],
        "precio": [total_precio],
        "Cambio Porcentual": [total_cambio_porcentual],
        "Promedio Acumulado": [total_promedio_acumulado],
        "Diferencia Precio": [total_diferencia_precio]
    })

    # Redondear los totales a dos decimales
    totales["precio"] = totales["precio"].round(2)
    totales["Cambio Porcentual"] = totales["Cambio Porcentual"].round(2)
    totales["Promedio Acumulado"] = totales["Promedio Acumulado"].round(2)
    totales["Diferencia Precio"] = totales["Diferencia Precio"].round(2)

    # Concatenar la fila de totales al DataFrame original
    df_final = pd.concat([df, totales], ignore_index=True)

    # Imprimir la tabla final
    print(tabulate(df_final, headers='keys', tablefmt='pretty', showindex=False))

    # Preguntar si desea exportar a CSV
    exportar = input("¿Desea exportar el resultado a un archivo CSV? (s/n): ")
    if exportar.lower() == 's':
        nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ")
        df_final.to_csv(f"{ruta_csv}/{nombre_archivo}.csv", index=False)
        print(f"Datos exportados a {nombre_archivo}.csv")

# Llamar a la función con el DataFrame
analizar_precios(df)
