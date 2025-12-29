# While
contador = 0
while contador < 10:
  print(contador)
  contador += 1

# Utilizando el break para salir de un bucle
contraseña = input("Introduce la contraseña: ")
while contraseña != "contraseña":
  contraseña = input("Introduce la contraseña: ")
  if contraseña == "contraseña":
    print("Contraseña correcta")
    break

# Utilizando el continue para saltar una iteración
contador = 0
while contador < 10:
  contador += 1
  if contador == 5:
    continue
  print(contador)

# Utilizando el else para ejecutar un código cuando el bucle termina
contador = 0
while contador < 10:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# Ejercicio práctico
numero = -1

while numero < 0:
  try:
    numero = int(input("Introduce un número: "))
    if numero < 0:
      print("El número es negativo")
  except ValueError:
    print("Introduce un número válido")

print(f"El número es {numero}")