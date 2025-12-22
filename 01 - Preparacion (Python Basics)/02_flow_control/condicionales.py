# Condicionales

import os
os.system("cls")

# Sentencia if simple

edad_usuario = int(input("Ingresa tu edad: "))
edad_requerida = 18

if edad_usuario >= edad_requerida:
    print("Puedes votar")

# Sentencia if-else

contraseña = "123456"
contraseña_usuario = input("Ingresa tu contraseña: ")

if contraseña == contraseña_usuario:
    print("Acceso concedido")
else:
    print("Acceso denegado")

# Sentencia if-elif-else

dia = "Lunes"

if dia == "Lunes":
    print("Es Lunes")
elif dia == "Martes":
    print("Es Martes")
elif dia == "Miercoles":
    print("Es Miercoles")
elif dia == "Jueves":
    print("Es Jueves")
elif dia == "Viernes":
    print("Es Viernes")
elif dia == "Sabado":
    print("Es Sabado")
elif dia == "Domingo":
    print("Es Domingo")
else:
    print("Es otro dia")

# Operadores logicos (and, or, not)

# and
edad = 18
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")
    
# or
if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

# not

es_fin_de_semana = True

if not es_fin_de_semana:
    print("Puedes ir a la playa")
else:
    print("No puedes ir a la playa")

# Operadores ternarios
ternario = "Verdadero" if 5 > 3 else "Falso"