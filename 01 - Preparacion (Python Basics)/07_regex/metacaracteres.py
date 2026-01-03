# Meta Caracteres

import re

# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares

# 1. El Punto (.) -> coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, ! Hóla de nuevo, H0la otra vez."
pattern = "H.la"

found = re.findall(pattern, text)

if found:
  print(found)
else:
	print("No se ha encontrado el patron")

# Como usar la barra invertida para anular el significado especial de un simbolo
text = "Mi casa es blanca, y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)

# \d: coincide con cualquier digito (0-9)

text = "El numero es 123456789"
found = re.findall(r"\d{9}", text)

print(found)

# Ejercicio: Detectar si hay un numero de españa en el texto con el prefijo +34

text = "Mi numero de telefono es: +34 567890331"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: print(f"Se encontro el numero de telefono: {found.group()}")

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualquier espacio en blanco (espacio, tabulacion, salto de linea)

text = "Hola mundo\nComo estas?\t"
pattern = r"\s"
found = re.findall(pattern, text)
print(found) 

# \^: Coincide con el principio de una cadena
username = "%423_name"
pattern = r"^\w" # validar nombre de usuario
valid = re.search(pattern, username)

if (valid): 
  print("El nombre de usuario es valido.")
else:
  print("El nombre de usuario no es valido.") 

# {numero_inicial, numero_final}: Rango de digitos permitidos

phone = "+34 688999999"
pattern = r"^\+\d{2,3} \d{9}"
valid = re.search(pattern, phone)

if valid: print(f"El numero de telefono es valido {valid.group()}")

# $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"
valid = re.search(pattern, text)

if valid: print("La cadena de texto acaba en mundo")
else: print("La cadena de texto no acaba en mundo")

# Ejercicio 2
# Validar que un correo sea de gmail

text = "pipe@gmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

if valid: print("El correo es gmail valido")
else: print("El correo no es valido")

# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"
found = re.findall(pattern, text)
print(found)

# |: Coincidir con una opcion u otra

frutas = "Manzana, Pera, Platano, Aguacate, Uvas"
pattern = r"pera|platano"
found = re.findall(pattern, frutas, re.IGNORECASE)
print(found)