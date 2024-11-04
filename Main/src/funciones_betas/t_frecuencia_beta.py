import pandas as pd
from tabulate import tabulate

def analizar_precios(df):
    """
    Analiza los precios mensuales y calcula el cambio porcentual y el promedio acumulado.
    
    Args:
    df (pd.DataFrame): DataFrame que contiene las columnas 'fecha' y 'precio'.
    """
    
    # Calcular el cambio porcentual
    df["Cambio Porcentual"] = df["precio"].pct_change() * 100
    
    # Rellenar el primer mes con 0
    df["Cambio Porcentual"].fillna(0, inplace=True)

    # Calcular el promedio acumulado de cambio porcentual
    df["Promedio Acumulado"] = df["Cambio Porcentual"].expanding().mean()

    # Calcular el total de precios
    total_precio = df["precio"].sum()
    total_cambio_porcentual = df["Cambio Porcentual"].sum()
    total_promedio_acumulado = df["Promedio Acumulado"].mean()

    # Agregar una fila de totales
    totales = pd.DataFrame({
        "fecha": ["Total"],
        "precio": [total_precio],
        "Cambio Porcentual": [total_cambio_porcentual],
        "Promedio Acumulado": [total_promedio_acumulado]
    })

    # Concatenar la fila de totales al DataFrame original
    df_final = pd.concat([df, totales], ignore_index=True)

    # Imprimir la tabla final
    print(tabulate(df_final, headers='keys', tablefmt='pretty', showindex=False))

    # Preguntar si desea exportar a CSV
    exportar = input("¿Desea exportar el resultado a un archivo CSV? (s/n): ")
    if exportar.lower() == 's':
        nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ")
        df_final.to_csv(f"{nombre_archivo}.csv", index=False)
        print(f"Datos exportados a {nombre_archivo}.csv")

# Ejemplo de uso
data = {
    "fecha": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"],
    "precio": [24.7, 26.87, 25.68, 22.39, 22.39, 61.74, 52.09, 50.03, 51.62, 49.35]
}
df = pd.DataFrame(data)

# Llamar a la función con el DataFrame
analizar_precios(df)
