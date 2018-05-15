
def first_not_repeating_char(caracteres):
    letras_vistas = {}

    for idx, letra in enumerate(caracteres):
        if letra not in letras_vistas:
            letras_vistas[letra] = (idx, 1)
        else:
            letras_vistas[letra] = (letras_vistas[letra][0], letras_vistas[letra][1] + 1)

    for key, value in letras_vistas.items():
        if value[1] == 1:
            return key

    return -1


caracteres = str(input("Ingresa una cadena de texto: "))

resultado = first_not_repeating_char(caracteres)

if resultado == -1:
    print("Todos los caracteres se repiten")
else:
    print("El primero q NO repite es {}".format(resultado))
