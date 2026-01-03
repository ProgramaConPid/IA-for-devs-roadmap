from bs4 import BeautifulSoup
import requests

url = "https://www.apple.com/co/macbook-air/"

response = requests.get(url)

if response.status_code == 200:
  print("La peticion fue exitosa")

  soup = BeautifulSoup(response.text, 'html.parser')

  print(soup.prettify()) # Prettify() -> Formatea el html de la web y lo devuelve organizado
  title_tag = soup.title

  if title_tag:
    print(f"El titulo de la web es: {title_tag.string}")

  # Obtener un elemento especifico
  span_element = soup.find('span', class_="ac-gf-directory-column-section-title-text")
  if span_element:
    print(f"Se encontro el elemento span: {span_element.string}")

  # Encontrar todos los h2 de la web
  titles_h2 = soup.find_all('h2')
  for t in titles_h2:
    print(f"El texto del titulo es: {t.string}")

  # Recuperar las notas del footer
  list_footer = soup.find('ol')

  for li in list_footer.find_all('li'):
    print(li)

    




