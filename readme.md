# Proyecto de Web Scraping y Almacenamiento de Datos en JSON

## Cómo empezar

### Disclaimers

Antes de comenzar a trabajar con este proyecto, ten en cuenta lo siguiente:

- Este proyecto tiene como objetivo aprender sobre web scraping y el manejo de datos en formato JSON. 
- La implementación original involucraba el uso de una base de datos, pero debido a problemas técnicos, se ha decidido utilizar JSON como método de almacenamiento.
- Este código puede no funcionar en todos los sistemas operativos. Si encuentras algún error, siéntete libre de adaptarlo a tus necesidades.
- La estructura del proyecto está en fase de reestructuración y puede cambiar conforme se avanza en el desarrollo.
- Este proyecto es para fines educativos y puede haber errores o fallas en la ejecución.

### Librerías

Este proyecto utiliza Python 3 (testeado con la 3.9.6) y las siguientes librerías:

- requests
- beautifulsoup4
- pandas

Para instalarlas, es recomendable que inicies un entorno virtual de Python. Puedes hacerlo ejecutando el siguiente código en un terminal:

```bash
pip3 install virtualenv  # Para instalar el paquete  
cd carpeta/del/proyecto/  # Para ir a la carpeta del proyecto
python3 -m venv nombre_del_entorno  # Para crear el entorno virtual  
source nombre_del_entorno/bin/activate  # Para activar el entorno virtual  
```

Para instalar las librerías, utiliza el archivo `requirements.txt`:

```bash
pip3 install -r requirements.txt
```

### Programa

Una vez que tengas todas las librerías instaladas y con el entorno virtual activo (si decidiste crear uno), simplemente ejecuta el archivo principal escribiendo en un terminal:

```bash
cd carpeta/del/proyecto/
python3 main.py  # Ejecución del archivo principal
```

El programa iniciará el proceso de scraping de la página web, limpiará y transformará los datos, y luego los almacenará en un archivo JSON. Asegúrate de que la conexión a Internet esté activa y que la página web de destino esté disponible durante la ejecución.

## Estado Actual

El proyecto se encuentra en una fase de reestructuración, enfocándose en el almacenamiento de datos en formato JSON en lugar de en una base de datos. Esta decisión busca simplificar el manejo de datos y facilitar el aprendizaje sobre las técnicas de web scraping y la gestión de datos.

## Temas a Aprender

Es importante continuar aprendiendo sobre bases de datos y su funcionamiento, ya que el objetivo original incluía almacenar los datos en una base de datos. Aquí hay algunos temas sugeridos:

- Fundamentos de bases de datos relacionales (SQL).
- Diseño de esquemas de bases de datos.
- Consultas y manipulación de datos en SQL.
- Uso de ORMs (Object-Relational Mappers) como SQLAlchemy.
- Introducción a bases de datos NoSQL (MongoDB, etc.).

## Conclusión

Este proyecto tiene como finalidad mejorar el manejo y almacenamiento de datos relacionados con Pokémon, y se están tomando nuevas direcciones para lograrlo mediante el uso de JSON. Se espera que esta reestructuración permita una mejor gestión de los datos y un avance significativo en el desarrollo del proyecto.

--- 

¿Te gustaría hacer algún cambio o agregar algo más a este README?