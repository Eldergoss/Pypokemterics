import os 
import json

ruta ="/home/david/Documentos/pypokemtrics/Main/data/json/paradox rift/paradox rift 2024.json"
with open (ruta ,"r") as archivo : 
    data = json.load(archivo)


print(f"nombre:{data[cartas][mes]}")
