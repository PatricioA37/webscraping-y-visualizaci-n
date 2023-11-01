import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.sii.cl/valores_y_fechas/utm/utm2023.htm'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Encuentra todas las celdas en la tabla
    UTM = soup.find_all('td')
    mes = soup.find_all('th')

    if len(UTM) > 0 and len(mes) > 0:
        # Asegúrate de que ambas listas tengan la misma longitud
        min_length = min(len(UTM), len(mes))
        UTM_lista = [cell.get_text() for cell in UTM[:min_length]]
        mes_lista = [cell.get_text() for cell in mes[:min_length]]

        # Crear un DataFrame a partir de las listas de UTM y Mes
        df = pd.DataFrame({'UTM': UTM_lista, 'Mes': mes_lista})

        # Guardar el DataFrame en un archivo CSV
        df.to_csv('datos_SII.csv', index=False, encoding="utf-16")

        print("Datos guardados en el archivo datos_SII.csv")
    else:
        print("No se encontraron celdas en la tabla")
else:
    print("Error en la solicitud")
