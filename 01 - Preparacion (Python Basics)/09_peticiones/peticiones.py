# Como hacer peticiones a APIs con python
# Con y sin dependencias

# 1. Sin dependencias
import requests
import urllib.request
import json 

api_posts = "https://jsonplaceholder.typicode.com/posts"

try:
  response = urllib.request.urlopen(api_posts)
  data = response.read()
  json_data = json.loads(data.decode("utf-8"))
  print(json_data)
  response.close()
except urllib.error.URLError as e:
  print(f"Error en la solicitud: {e.reason}")


# 2. Con dependencias (requests)
# Metodo GET
print("GET:")

import requests

api_posts = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_posts)
json = response.json()
print(json[0])

# Metodo POST
print("POST:")

try:
  api_posts = "https://jsonplaceholder.typicode.com/posts"
  input={
    "title": "pepe",
    "body": "botellas",
    "userId": 5
  }
  response = requests.post(api_posts, json=input)
  print(response.status_code) # 201
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")  

# Metodo PUT
print("PUT: \n")

try:
  api_posts = "https://jsonplaceholder.typicode.com/posts/1"
  input={
    "title": "foo",
    "body": "bar",
    "userId": 1
  }
  response = requests.put(api_posts, json=input)
  print(response.status_code) # 200  
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")  