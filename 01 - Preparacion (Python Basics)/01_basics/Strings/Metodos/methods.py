# Slicing

text = "Hello, world!"
print(text[1:6]) # Output: ell
print(text[:5]) # Output: Hello
print(text[2:]) # Output: llo, world!

# Convertit a mayusculas
print(text.upper())

# Convertit a minusculas
print(text.lower())

# Eliminar espacios en blanco
print(text.strip()) 

# Reemplazar una subcadena
print(text.replace("world", "Python"))

# Dividir la cadena (el separador por defecto es el espacio)
print(text.split(",")) # Output: ['Hello', 'world!']

# ----------- Formateo de cadenas ----------- #

# Formateo de cadenas con el metodo format()
text = "Hello, {}!".format("world")
print(text)

# Formateo de cadenas con el metodo f-string (Python 3.6+)
name = "Pedro"
text = f"Hello, {name}!"
print(text)
