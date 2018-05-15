"""
Funciones de cadenas de texto 'str' Ingresamos
un nombre y le hacemos modificaciones
"""
nombre = str(input("Ingresa el nombre: "))
print("-"*20)

# Mostrando el nombre
print(nombre)

# Mostrando el nombre a la inversa
print(nombre[::-1])

# string en mayusculas
print(nombre.upper())

# string en minusculas
print(nombre.lower())

# Capitalize string
print(nombre[:1].upper() + nombre[1:].lower())

# Mostrando el nombre con letras desordenadas
import random
print("".join(random.sample(nombre, len(nombre))))

# Mostrando largo de la cadena
print("El largo del texto es: " + str(len(nombre)))

# Separando cadena en caracteres
letras = []
for char in nombre:
    letras.append(char)

print(letras)

