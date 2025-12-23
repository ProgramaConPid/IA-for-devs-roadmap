# While
contador = 0
while contador < 10:
    print(contador)
    contador += 1

# Utilizando el break
contraseña = str(input("Introduce la contraseña: "))
while contraseña != "contraseña":
    contraseña = str(input("Introduce la contraseña: "))
    if contraseña == "contraseña":
        print("Contraseña correcta")
        break

# Utilizando el continue
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print(contador)