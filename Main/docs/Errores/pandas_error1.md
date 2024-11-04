# Resumen de Errores y Soluciones

## 1. **Error al usar `replace()` en columnas de cadenas**
   - **Descripción**: Intentar reemplazar un año que se encuentra en una cadena, sin asegurarse de que el valor sea tratado como texto.
   - **Solución**: Usar `str.replace()` para reemplazar adecuadamente dentro de una columna de tipo cadena.
     ```python
     df["fecha"] = df["fecha"].str.replace("2024", " ")
     ```

## 2. **Reemplazo no reflejado en el DataFrame**
   - **Descripción**: Al usar `replace()`, se asigna el resultado a una nueva variable sin actualizar el DataFrame original.
   - **Solución**: Actualizar directamente la columna en el DataFrame.
     ```python
     df["fecha"] = df["fecha"].replace("2024", " ", regex=False)
     ```

## 3. **No se importó correctamente `tabulate`**
   - **Descripción**: Intentar usar `tabulate` sin haberlo importado correctamente.
   - **Solución**: Asegurarse de importar `tabulate` de esta manera:
     ```python
     from tabulate import tabulate
     ```

## 4. **Formato de año no considerado**
   - **Descripción**: Si se esperaba que el año estuviera en el DataFrame y no se consideró.
   - **Solución**: Asegurarse de extraer y trabajar con los elementos adecuados en el JSON.
     ```python
     precio_por_mes[f"{mes} {año}"] = carta["precio"]
     ```

## 5. **Datos no encontrados en el JSON**
   - **Descripción**: Al buscar un ID de carta que no existe en el JSON.
   - **Solución**: Incluir un mensaje informativo si el ID no se encuentra.
     ```python
     if not precio_por_mes:
         print("ID de carta no encontrada")
     ```

## 6. **Visualización del DataFrame**
   - **Descripción**: No se utilizó un método adecuado para imprimir el DataFrame en un formato legible.
   - **Solución**: Usar `tabulate` para una visualización clara.
     ```python
     print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
     ```

---

Este resumen puede ayudarte a identificar y corregir errores comunes en el manejo de pandas y la visualización de datos.
