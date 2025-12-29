# Range(inicio, fin)

print("Range tradicional:")

for num in range(5, 20):
  print(num)

print("\nRange con paso:")

# Range (inicio, fin, paso)
for num in range(5, 20, 2):
  print(num)

# Range con numeros negativos
print("\nRange con negativos:")

for num in range(-10, 0):
  print(num)

# Range con cuentra atras
print("\nRange con cuenta atras:")
for num in range(10, 0, -1):
  print(num)

# Convertir un range a una lista
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)