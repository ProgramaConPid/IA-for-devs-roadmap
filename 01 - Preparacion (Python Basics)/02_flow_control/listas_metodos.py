# Insertar elementos en una lista -> append
lista1 = [1, 2, 3, 4]
print(lista1)

# Insertar elementos en una lista en una posicion especifica -> insert
lista2 = [1, 2, 3]
lista2.insert(1, 5) # Inserta el elemento en la posicion 1
print(lista2)

# Agregar elementos al final de la lista -> extend
lista1.extend([6, 7, 8])
print(lista1)

# Eliminar la primera aparicion de un elemento -> remove
lista1.remove(1)
print(lista1)

# Eliminar por indice o el ultimo elemento -> pop
lista1.pop(2) # Elimina el elemento en la posicion 2
print(lista1)

lista4 = [1, 2, 3, 4, 5]
lista4.pop() # Elimina el ultimo elemento
print(lista4)

# Eliminar todos los elementos -> clear
lista1.clear()
print(lista1)

# Ordenar la lista -> sort
lista1 = [3, 1, 2]
lista1.sort()
print(lista1)

# Crear una copia ordenada de la lista original -> sorted
lista2 = [7, 2, 9, 0, 2, 5]
sorted_numbers = sorted(lista2)
print(sorted_numbers)

# Verificar cuantas veces se repite un elemento -> count
lista3 = [1, 2, 3, 4, 5, 2, 2]
print(lista3.count(2))
