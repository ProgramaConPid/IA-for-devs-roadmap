# Scraping -> Extraer datos de un sitio web

import requests
import re

url = "https://www.apple.com/co/macbook-air/"

response = requests.get(url)

if response.status_code == 200:
  print("La peticion fue exitosa")

  html = response.text

  price_pattern = r'<span class="ac-gf-directory-column-section-title-text">(.*?)</span>'
  match = re.search(price_pattern, html)

  if match: print(f"Patron encontrado con exito: {match.group(1)}")
else: 
  print("Algo fallo en la peticion.")
  