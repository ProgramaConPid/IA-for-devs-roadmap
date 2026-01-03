import re

# []: Coincide con cualquier caracter dentro de los corchetes

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)

if match: 
  print("El nombre de usuario es valido:", match.group())
else:
  print("El nombre de usuario no es valido")

# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran fan pan ban omniman"
pattern = r"\b[mbf]an\b"
matches = re.findall(pattern, text)
print(matches)