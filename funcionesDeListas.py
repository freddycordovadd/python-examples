"""
Funciones basicas de una lista de numeros
"""

# Lista de numeros
numeros=[100,33,16,15,16,2,99,45,16,54]

# Imprimiendo el mayor de los numeros
print(str(max(numeros)))

# agregando 112 a la lista
numeros.append(112)
print(numeros)

print(str(max(numeros)))
print("-"*20)

# conteo de un elemento/todos los elementos
print(numeros.count(16))
print(len(numeros))

# Saber el indice de la primera coincidencia de un elemento
# Con index el elemento tiene q existir, sino error
print(numeros.index(16))

# insertar en un indice

numeros.insert(2,25)
print(numeros)
print("-"*20)

# hacer un pop con el ultimo obj de la lista

print(numeros.pop())
print(numeros)

# pop en indice particular

print(numeros.pop(2))
print(numeros)

# reversa a la lista

numeros.reverse()
print(numeros)

# ordenar la lista de menor a mayor y viceversa

numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

# Promedio de los numeros
print(sum(numeros)/len(numeros))

# Crear nueva lista derivada de la lista numeros

lista2 = [(num * 100) for num in numeros]
print(lista2)

# Confirmar si un dato esta en la lista
print(100 in numeros)
print("Hola" in numeros)

