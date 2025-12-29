# Diccionarios -> Colecciones de pares calve-valor

# Ejemplo clasico de un diccionario

persona = {
  "nombre": "Felipe",
  "edad": 25,
  "is_developer": True,
  "calificaciones": [5, 7, 9],
  "redes_sociales": {
    "twitter": "felp123",
    "tiktok": "programaconpid",
    "facebook": "Felipe Marin"
  }
}


# Acceder a los valores del diccionario
print(persona["nombre"])
print(persona["calificaciones"][0])
print(persona["redes_sociales"]["twitter"])

# Cambiar valores al acceder
persona["nombre"] = "Pedro"
persona["redes_sociales"]["twitter"] = "pedrito123"

# Eliminar completamente una propiedad
del persona["calificaciones"][0]

# Recuperar un valor y eliminarlo del diccionario
is_developer = persona.pop("is_developer")
print(f"is_developer: {is_developer}")
print(f"persona: {persona}")

# Sobreescribir un diccionario con otro diccionario
a = { "name": "Daniel", "age": 23}
b = { "name": "Lucia", "es_estudiante": True }

a.update(b)
print(f"a: {a}")

# Comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True

# Obtener todas las claves
print(persona.keys())

# Obtener todos los valores
print(persona.values())

# Obtener todas las claves y valores
print(persona.items())

# Iterar un diccionario por clave y valor
for key, value in persona.items():
  print(f"{key}: {value}")

# Obtener el valor de una propiedad
print(persona.get("nombre"))