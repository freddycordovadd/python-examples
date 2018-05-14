# Juego de la serie The Big Bang Theory
# Piedra, Papel, Tijeras, Lagarto, Spock
import random, time

# Elecciones disponibles para el juego
elecciones = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"]


def opcion_usuario():
    """
    Solicita la opcion del usuario entre el 1 y 5 (Pi, Pa, Ti, La, Sp)
    :return: La opcion del usuario en numero entero
    """
    print("Que escoges ???")
    print("Escoge 1 para: Piedra")
    print("Escoge 2 para: Papel")
    print("Escoge 3 para: Tijeras")
    print("Escoge 4 para: Lagarto")
    print("Escoge 5 para: Spock")
    print("Escoge 9 para ver las reglas del juego")
    time.sleep(0.5)
    eleccion = int(input("Cual es tu eleccion: "))
    while eleccion == 9:
        reglas()
        eleccion = int(input("Cual es tu eleccion: "))
    print("----------------------------")
    return eleccion


def opcion_maquina():
    """
    Genera la opcion de la maquina, aleatorio de 1 a 5
    :return: La opcion de la maquina
    """
    eleccion = random.randint(1, 5)
    return eleccion


def enfrentar(usuario, maquina):
    """
    Hace que se enfrenten las 2 partes con condicionales if
    :param usuario: Eleccion del usuario
    :param maquina: Eleccion de la maquina
    :return: No retorna, imprime respuesta
    """
    print("Tu, usuario humano escogiste... " + elecciones[usuario - 1])
    print("La Maquina todo poderosa escogio... " + elecciones[maquina - 1])
    time.sleep(1)
    print("----------------------------")

    if usuario == maquina:
        print("Iguales, fue un empate!")

    if usuario == 1:
        # Si el usuario escoge 1: "Piedra"
        if maquina == 2:
            print("Papel cubre la Piedra")
            print("Perdiste!")
        elif maquina == 3:
            print("Piedra rompe Tijeras")
            print("Ganaste!")
        elif maquina == 4:
            print("Piedra aplasta Lagarto")
            print("Ganaste!")
        elif maquina == 5:
            print("Spock desintegra la Piedra")
            print("Perdiste!")
    elif usuario == 2:
        # Si el usuario escoge 2: "Papel"
        if maquina == 1:
            print("Papel cubre la Piedra")
            print("Ganaste!")
        elif maquina == 3:
            print("Tijeras cortan Papel")
            print("Perdiste!")
        elif maquina == 4:
            print("Lagarto come Papel")
            print("Perdiste!")
        elif maquina == 5:
            print("Papel refuta a Spock")
            print("Ganaste!")
    elif usuario == 3:
        # Si el usuario escoge 3: "Tijeras"
        if maquina == 1:
            print("Piedra rompe Tijeras")
            print("Perdiste!")
        elif maquina == 2:
            print("Tijeras cortan Papel")
            print("Ganaste!")
        elif maquina == 4:
            print("Tijeras matan Lagarto")
            print("Ganaste!")
        elif maquina == 5:
            print("Spock destruye Tijeras")
            print("Perdiste!")
    elif usuario == 4:
        # Si el usuario escoge 4: "Lagarto"
        if maquina == 1:
            print("Piedra aplasta Lagarto")
            print("Perdiste!")
        elif maquina == 2:
            print("Lagarto come Papel")
            print("Ganaste!")
        elif maquina == 3:
            print("Tijeras matan Lagarto")
            print("Perdiste!")
        elif maquina == 5:
            print("Lagarto envenena Spock")
            print("Ganaste!")
    elif usuario == 5:
        # Si el usuario escoge 5: "Spock"
        if maquina == 1:
            print("Spock desintegra la Piedra")
            print("Ganaste!")
        elif maquina == 2:
            print("Papel refuta a Spock")
            print("Perdiste!")
        elif maquina == 3:
            print("Spock destruye Tijeras")
            print("Ganaste!")
        elif maquina == 4:
            print("Lagarto envenena Spock")
            print("Perdiste!")


def reglas():
    """
    Explica las reglas del juego, solo eso
    :return: No retorna nada
    """
    print("----------------------")
    print("Tijeras cortan Papel")
    print("Papel cubre Piedra")
    print("Piedra aplasta Lagarto")
    print("Lagarto envenena Spock")
    print("Spock rompe Tijeras")
    print("Tijeras matan Lagarto")
    print("Lagarto come Papel")
    print("Papel refuta Spock")
    print("Spock desintegra Piedra")
    print("Piedra rompe Tijeras")
    print("----------------------")


# Inicio del programa
print("PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK !")

time.sleep(1)
user = opcion_usuario()
machine = opcion_maquina()

time.sleep(1)
enfrentar(user, machine)

