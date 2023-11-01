import requests
import pandas as pd

# Definir la URL
url = "https://agrometeorologia.cl/assets/db/items-resumen.json?_=1694699167145"

try:
    # Realizar una solicitud GET a la URL
    response = requests.get(url)
    response.raise_for_status()  # Verificar si la solicitud fue exitosa

    # Parsear la respuesta JSON
    data = response.json()

    # Convertir el JSON en un DataFrame de Pandas
    df = pd.DataFrame(data)

    # Especificar el nombre del archivo CSV de salida
    archivo_csv = "datos_agrometeorologia.csv"

    # Guardar el DataFrame en un archivo CSV
    df.to_csv(archivo_csv, index=False)

    print(f"Datos guardados en {archivo_csv}")

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud HTTP: {str(e)}")
except ValueError as e:
    print(f"Error al parsear el JSON: {str(e)}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {str(e)}")
