# Funciones

"""
Estructura de una funcion

def nombre_funcion(parametro1, parametro2):
  # cuerpo de la funcion
  return retorno_de_la_funcion
"""

def saludar():
  print("Hola")

# Llamado de la funcion
saludar()

# Con parametros

def saludar_usuario(usuario):
  print(f"Hola {usuario}")

saludar_usuario("Pepe")
saludar_usuario("Rocio")
saludar_usuario("Carlos TL")

# Con mas parametros

def sumar(a, b) -> str:
  suma = a + b
  return f"resultado: {suma}"

resultado = sumar(1, 2)
print(resultado)

# Documentar las funciones con docstrings

def restar(a, b):
  """Resta dos numeros"""
  return a - b

print(restar.__doc__)

# Parametros por defecto (parametro = valor)

def saludar_pepe(usuario = "Pepe"):
  return f"Hola {usuario}"

print(saludar_pepe())

# Argumentos de longitud de variable

def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero

  return f"resultado: {suma}"

print(sumar_numeros(1, 2, 3, 4, 5))

# Argumentos de clave valor variable **kwargs

def mostrar_informacion(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

mostrar_informacion(nombre="Pepe", edad=23, is_developer=True)
mostrar_informacion(nickname="midu", fav_color="Green", is_developer=False)
