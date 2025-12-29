"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

def count_eggs_carnivores(eggs_list) -> str | int:

  total_eggs = 0

  if len(list) == 0: return 0

  for e in eggs_list:
    if e % 2 == 0:
      total_eggs += e

  return f"Amount: {total_eggs}"

result = count_eggs_carnivores([1,2,3,4,5,6,7,8,9])
print(result)