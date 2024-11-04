Aquí tienes un ejemplo de un archivo Markdown (README.md) que documenta el error que experimentaste y proporciona el script corregido.

```markdown
# Documentación del Error y Solución

## Descripción del Problema

Al intentar ejecutar un script de Python para cargar un archivo JSON, se produjo un error debido a que no se había importado el módulo `os`, que es necesario para verificar la existencia del archivo.

## Error Encontrado

Al ejecutar el siguiente script:

```python
import json

# Ruta relativa del archivo JSON
ruta_archivo = 'Main/src/Extraccion/json/Link_Container.json'

# Verificar si el archivo existe
if os.path.exists(ruta_archivo):  # Esto causaba un NameError
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print("Expansión:", data["Expansion"])
        print("Links:")
        for link in data["links"]:
            print(link)
    except json.JSONDecodeError:
        print("Error: El archivo no está en un formato JSON válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
else:
    print("Error: El archivo no se encontró en la ruta especificada.")
```

Se produjo el siguiente error:
```
NameError: name 'os' is not defined
```

## Solución

Para solucionar este error, se debe importar el módulo `os` al inicio del script. A continuación se muestra el script corregido:

```python
import json
import os  # Importar el módulo os

# Ruta relativa del archivo JSON
ruta_archivo = 'Main/src/Extraccion/json/Link_Container.json'

# Verificar si el archivo existe
if os.path.exists(ruta_archivo):
    try:
        # Cargar el JSON desde el archivo
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Imprimir la expansión
        print("Expansión:", data["Expansion"])

        # Imprimir los links
        print("Links:")
        for link in data["links"]:
            print(link)

    except json.JSONDecodeError:
        print("Error: El archivo no está en un formato JSON válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
else:
    print("Error: El archivo no se encontró en la ruta especificada.")
```

## Conclusión

Siempre asegúrate de importar todos los módulos necesarios en tu script para evitar errores como `NameError`. Verificar la existencia de archivos antes de operar sobre ellos es una buena práctica para asegurar que tu código funcione sin problemas.
```

### Instrucciones
- Guarda este contenido en un archivo llamado `README.md`.
- Puedes añadir más detalles o secciones según sea necesario. 

Si necesitas más ayuda, ¡hazmelo saber!