aqui iran posibles funciones de un manejador de datos en python
import json

# Ruta del archivo que contiene los datos JSON
ruta_archivo = "/ruta/a/tu/archivo/datos.json"  # Cambia esto a la ruta correcta

# Función para cargar y formatear el JSON
def cargar_y_mostrar_json():
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        datos = json.load(file)
    
    # Imprimir los datos en un formato legible
    print(json.dumps(datos, indent=4, ensure_ascii=False))

# Llamar a la función
cargar_y_mostrar_json()
