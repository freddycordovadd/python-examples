"""
Ejemplo de continue, break y pass
para ciclos for
"""

# continue
"""
La declaracion "continue", continua con la siguiente
iteracion del ciclo, ignorando el codigo faltante del bloque
"""

for numero in range(1, 10):
    # buscando multiplos de 3
    if numero % 3 == 0:
        print("Toco un multiplo de 3")
        continue #regresa al for para continuar el ciclo
        print("esto se ignora, nunca pasara")
    print("El numero: " + str(numero) + " NO es multiplo de 3")
    
print("---Fin del ejemplo---")


# break
"""
La declaracion "break", fuerza la salida del ciclo for sin importar
en que iteracion del ciclo se encuentre, tmb funciona para while
"""

for numero in range(1, 10):
    # buscando multiplos de 3
    if numero % 3 == 0:
        print("Toco un multiplo de 3")
        break #apenas encuentre un multiplo de 3, sale del for
        print("esto se ignora, nunca pasara")
    print("El numero: " + str(numero) + " NO es multiplo de 3")
    
print("---Fin del ejemplo---")
