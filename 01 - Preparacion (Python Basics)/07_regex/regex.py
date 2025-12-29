# Expresiones Regulares

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
  Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """

# 1. Importar el módulo re
import re

# 2. Crear un patrón
pattern = "Hola"

# 3. Texto de búsqueda 
text = "Hola mundo"

# 4. Buscar el patrón re.search(patron, texto a buscar el patron)
result = re.search(pattern, text)
print(result) 

if result:
  print("Encontrado")
else:
  print("No encontrado")

# re.group() -> Devuelve el texto encontrado
print(result.group())

# re.start() -> Devuelve el indice donde comienza el texto encontrado
print(f"Comienza en el indice: {result.start()}")

# re.end() -> Devuelve el indice donde termina el texto encontrado
print(f"Termina en el indice: {result.end()}")

# re.span() -> Devuelve el indice donde comienza y termina el texto encontrado
print(result.span())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
  print(f"El indice inicial de la coincidencia es: {found_ia.start()} y el final es: {found_ia.end()}")
else:
  print("No Encontrado")

text="Me gusta Python, Python es lo maximo, Aunque Python no es tan dificil, ojo con Python"
pattern = "Python"

# findall() -> Encontrar todas las ocurrencias de el patron
find_all = re.findall(pattern, text)
print(find_all)

# finditer() -> devuelve un iterador con todos los resultados de la busqueda
text="Me gusta Python, Python es lo maximo, Aunque Python no es tan dificil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
  print(match.group(), match.start(), match.end())

# re.IGNORECASE -> Ignora las mayusculas y minusculas
text = "Todo el mundo dice que la IA nos va a quitar el trabajo, Pero la ia no es tan mala. !Viva la Ia¡"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found)

# .sub() -> Reemplaza todas las coincidencias de un patron en un texto
text = "Hola Mundo, ! Hola de nuevo."
pattern = "Hola"
replacement = "Adios"
result = re.sub(pattern, replacement, text)
print(result)