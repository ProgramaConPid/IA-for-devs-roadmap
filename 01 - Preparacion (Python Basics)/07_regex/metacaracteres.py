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

# Cmo usar la barra invertida para anular el significado especial de un simbolo
text = "Mi casa es blanca, y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)