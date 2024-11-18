import requests
from bs4 import BeautifulSoup
import pandas as pd

# Paso 1: Hacer una solicitud a la página web
url = "https://www.bbc.com/news"
response = requests.get(url)

if response.status_code == 200:  # Comprobar si la página es accesible
    # Paso 2: Analizar el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Paso 3: Extraer los titulares de noticias
    headlines = []
    for item in soup.find_all('h3'):  # Cambia 'h3' según la etiqueta usada para los titulares
        headline = item.get_text(strip=True)
        if headline:
            headlines.append(headline)
    
    # Paso 4: Guardar los datos en un archivo CSV
    df = pd.DataFrame(headlines, columns=["Headline"])
    df.to_csv("news_headlines.csv", index=False, encoding="utf-8")
    print("¡Noticias guardadas en 'news_headlines.csv'!")
else:
    print("Error al acceder a la página:", response.status_code)