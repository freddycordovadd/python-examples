
import random

lista_palabras = ["proyecto",
            "plataforma",
            "datos",
            "cambios",
            "contenido",
            "informacion",
            "alumno",
            "codigo",
            "graficos",
            "descargar",
            "actualizar",
            "cronograma",
            "archivo",
            "excelente"]


images = ['''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========''', '''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========''']


def esconder(palabra):
    """
    Este metodo convierte la palabra en '-' y la
    introduce dentro de una lista
    :param palabra: palabra secreta del juego
    :return: palabra escondida en formato lista
    """
    palabra_escondida = "-" * len(palabra)
    p_escondida = []
    for char in palabra_escondida:
        p_escondida.append(char)
    return p_escondida


def buscar_indices(word, letra):
    """
    Este metodo verifica cada caracter de la palabra y si encuentra
    una coincidencia, pone el indice dentro de una lista
    :param word: palabra secreta del juego
    :param letra: letra ingresada por el usuario
    :return: lista de indices que coinciden con la letra ingresada
    """
    contador = 0
    indices = []
    for i in word:
        if i == letra:
            indices.append(contador)
        contador += 1
    return indices


def mostrar_pantalla(contador):
    """
    Muestra la respectiva pantalla de la lista images
    segun a como vaya el numero en la variable contador
    :param contador: para este caso es el indice de las pantallas
    :return: no retorna nada
    """
    print(images[contador])


def run():
    """
    Inicio del juego, crea las palabras
    y comienza el ciclo del juego
    :return: no retorna nada
    """
    # Escogiendo la palabra de la lista y escondiendola
    palabra = random.choice(lista_palabras)
    p_escondida = esconder(palabra)

    # Solo dejar esto para las pruebas
    # print("Trampa, la palabra es ... " + palabra)

    contador = 0
    while True:
        mostrar_pantalla(contador)
        print("")
        print(p_escondida)
        letra = str(input("Ingresa una letra: "))
        print("---- * ---- * ---- * ---- * ---- * ---- *")
        indices = buscar_indices(palabra, letra)

        # esto valida si el jugador perdio
        if len(indices) == 0:  # si la letra no coincidio con ningun caracter
            contador += 1
            if contador == 6:
                mostrar_pantalla(contador)
                print("Perdiste!! Estas ahorcado, la palabra era: " + palabra)
                break

        # Cambio de '-' por letra
        for i in indices:
            p_escondida[i] = letra
        indices = []

        # Verificar si el usuario gano
        if "-" in p_escondida:
            continue
        else:
            print(p_escondida)
            print("Felicidades, eres un ganador!")
            break
    print("--- FIN DEL JUEGO ---")


# Aqui comienza el codigo
print("----- BIENVENIDO AL JUEGO DE AHORCADO -----")
run()
