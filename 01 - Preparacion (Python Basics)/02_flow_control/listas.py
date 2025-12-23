# Creacion de listas

lista = [1, 2, 3, 4, 5]
print(lista)

# Lista de listas
lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista2)

# Acceso a elementos de la lista
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista2[-1]) # Ultimo elemento de la lista

# Acceso a elementos de la lista de listas
print(lista2[0][0])
print(lista2[0][1])
print(lista2[0][2])
print(lista2[1][0])
print(lista2[1][1])
print(lista2[1][2])
print(lista2[2][0])
print(lista2[2][1])
print(lista2[2][2])

# Modificacion de elementos de la lista
lista[0] = 10
print(lista)

# Eliminacion de elementos de la lista
lista.remove(10)
print(lista)

# Longitud de la lista
print(len(lista))

# Recorrer la lista
for i in lista:
    print(i)

# Slicing -> Rebanado de listas [inicio:fin]
lista3 = [1, 2, 3, 4, 5, 6]
print(lista3[1:4]) # Output: [2, 3, 4]
print(lista3[:4]) # Output: [1, 2, 3, 4]
print(lista3[2:]) # Output: [3, 4, 5, 6]

# Crear copia de una lista
lista4 = lista.copy()
print(lista4)

# Devolver indices pares
print(lista[::2]) # Output: [1, 3, 5]

# Devolver indices al reves
print(lista[::-1]) # Output: [5, 4, 3, 2, 1]

# Añadir elementos a una lista (+)

lista1 = lista + [1, 2, 3]
print(lista1)

# Forma mas corta y eficiente
lista1 += [10, 20, 30]
print(lista1)
