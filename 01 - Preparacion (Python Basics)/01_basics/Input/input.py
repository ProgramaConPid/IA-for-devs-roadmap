# La funcion input() permite obtener datos del usuario
name = input("Ingresa tu nombre: ")
lastName = input("Ingresa tu apellido: ")

print(f"Bienvenido {name} {lastName}")

# Recibir un valor entero
age = int(input("Ingresa tu edad: "))
print(f"Tu edad es {age}")

# Recibir un valor decimal
height = float(input("Ingresa tu altura: "))
print(f"Tu altura es {height}")

# Recibir multiples valores en una sola linea
country, city = input("Ingresa tu pais y ciudad: ").split()
print(f"Tu pais es {country} y tu ciudad es {city}")
