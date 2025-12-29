# For

# Permite iterar sobre un iterable
frutas = ["Manzana", "Pera", "Platano"]

for fruta in frutas:
  print(fruta)

# Iterar sobre un string
cadena = "Pepemojica"
for caracter in cadena:
  print(caracter)

# enumerate() permite obtener el indice y elemento del iterable
for index, caracter in enumerate(cadena):
  print(f"El indice es {index} y el valor es {caracter}")

# Bucles anidados
numeros = [1, 2, 3]
letras = ["a", "b", "c"]
for numero in numeros:
  for letra in letras:
    print(f"{letra.upper()}{numero}")

# Break
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for i, animal in enumerate(animales):
  print(animal)
  if animal == "loro":
    print(f"el {animal} se encuentra en el indice {i}")
    break

# Comprension de listas (list comprehension)
comidas = ["Arroz con Huevo", "Frijoles", "Chunchurria", "Chorizo"]
comidas_mayus = [comida.upper() for comida in comidas]
print(comidas_mayus)

# Con condicionales
pares = [num for num in range(1, 11) if num % 2 == 0]
print(pares)