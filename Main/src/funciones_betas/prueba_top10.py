import os 
import pandas as pd
# Extraer la cadena de strings de resultado.txt
data = "/home/david/python_project/Graficas_beta/data_raw/resultado.txt2"

def suma():
    print("la suma es ")


# Inicialización de listas
pokemon_names = []
card_numbers = []
prices = []

# Leer el archivo e iterar sobre él
with open(data, "r", encoding='utf-8') as t:
    for line in t:
        # Dividir la línea en nombre y precio
        name, price = line.strip().split(": $")
        
        # Extraer el número de la carta (última palabra)
        number = name.split()[-1]
        
        # Extraer el nombre del Pokémon (todas las palabras excepto la última)
        name = " ".join(name.split()[:-1])
        
        # Agregar los datos a las listas
        pokemon_names.append(name)
        card_numbers.append(number)
        prices.append(float(price))
    
#convetir a diccionario
datadict = {
    "Pokemon_Name": pokemon_names,
    "Card_Number": card_numbers,
    "Price_Card": prices
}

print(datadict)


df = pd.DataFrame(datadict)
print (df)
