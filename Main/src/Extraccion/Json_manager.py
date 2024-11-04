import json
import os
from web_scrap.scrap import extrac_tittle, extract_top10  # Importar solo las funciones que se necesitan

# JSON donde irán el output limpio
container_json = "/home/david/Documentos/pypokemtrics/Main/data/json/paradox rift/Paradox rif 2023.json"

# Función de carga de JSON
def carga_json():
    container_ruta = "/home/david/Documentos/pypokemtrics/Main/data/json/links/Link_Container.json"
    try:
        with open(container_ruta, 'r', encoding="utf-8") as file:
            archivo = json.load(file)
        return archivo
    except FileNotFoundError:
        print(f"Error: El archivo {container_ruta} no se encontró.")
    except json.JSONDecodeError:
        print(f"Error: El archivo {container_ruta} no está bien formado.")

# Función de selección de links
def seleccionar_links(data, category, year):
    if category in data:
        year_key = f'links{year}'  # Crear la clave 'links2023', 'links2024', etc.
        if year_key in data[category]:  # Verificar si existen enlaces para ese año
            return data[category][year_key]
    return []  # Si no existe la categoría o enlaces, devolver lista vacía

# Función que itera sobre los links usando extrac_tittle y extract_top10
def ite(links, expansion):
    resultados = {
        "expansion": expansion,
        "cartas": []
    }
    
    for link in links:
        try:
            scrap = extrac_tittle(link)  # Extraemos el título del enlace
            scrapp = extract_top10(link)  # Extraemos el top 10 del enlace
            
            # Extraemos el mes y año del título
            mes_año = scrap.split(" ")  # Separar por espacios
            mes = mes_año[-2]  # Asumiendo que el mes está en la penúltima posición
            año = int(mes_año[-1])  # Asumiendo que el año está en la última posición
            
            cartas = []
            for carta in scrapp:
                partes = carta.split(": $")
                if len(partes) < 2:  # Verificar si hay al menos dos partes
                    continue
                nombre_id = partes[0].rsplit(" ", 1)  # Separar el nombre y ID
                nombre = " ".join(nombre_id[:-1])  # Todo menos el último elemento
                id_carta = nombre_id[-1]  # Último elemento es el ID
                precio = float(partes[1])  # Convertir el precio a float
                
                # Agregar la carta al diccionario
                cartas.append({
                    "nombre": nombre,
                    "id_carta": id_carta,
                    "precio": precio
                })
            
            # Agregar el mes y año a la lista de cartas
            resultados["cartas"].append({
                "mes": mes,
                "año": año,
                "cartas": cartas
            })

        except Exception as e:
            print(f"Error procesando el enlace {link}: {e}")

    return resultados  # Devolver los resultados

# Función para crear el JSON con el top 10
def crear_json_top_10(data):
    try:
        with open(container_json, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Inyección completa.")
    except Exception as e:
        print(f"Error al escribir el archivo JSON: {e}")

# Ejemplo de uso
data = carga_json()
if data:  # Asegurarse de que los datos se cargaron correctamente
    print("Datos cargados:", data)
    links_paradox_rift_2024 = seleccionar_links(data, 'paradox rift', '2023')
    print("Links seleccionados:", links_paradox_rift_2024)
    
    resultados = ite(links_paradox_rift_2024, "paradox rift")
    print("Resultados obtenidos:", resultados)
    
    crear_json_top_10(resultados)
