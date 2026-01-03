# Cuantificadores

# Se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena

import re

# *: Puede aparecer 0 o mas veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# +: Una o mas veces
text = "dddd aaa bb ccc aa ab"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

# ?: Cero o una vez
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 1
# Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern = r"\+?34 \d{9}"

# {n}: Exactamente n veces
text = "aaaaaa aa aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
print(matches)

# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 2
# Encuentra las palabras de mas de 4 letras
words = "ala casa arbol leon cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)