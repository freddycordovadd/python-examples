
# Busqueda binaria
"""
Optimiza las busquedas para tablas de grandes volumenes (millones
de filas) unicamente funciona con data numerica ordenada
"""


def b_binaria(numeros, n_to_find, low, high):
    if low > high:
        return False

    mid = int((low + high) / 2)

    if numeros[mid] == n_to_find:
        return True
    elif numeros[mid] > n_to_find:
        return b_binaria(numeros, n_to_find, low, mid - 1)
    else:
        return b_binaria(numeros, n_to_find, mid + 1, high)


numeros = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 38, 45, 49, 51, 60]

n_to_find = int(input("Ingresa un numero: "))

r = b_binaria(numeros, n_to_find, 0, len(numeros) - 1)

if r:
    print("el numero si existe")
else:
    print("el numero NO existe")

