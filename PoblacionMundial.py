
paises = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}


def agregar_pais(pais):
    eleccion = input("Quieres agregarlo ??? (s / si / n / no): ").lower()
    if eleccion == "s" or eleccion == "si":
        nueva_cantidad = int(input("*Cuantos millones de habitantes tiene: "))
        paises[pais] = nueva_cantidad
        print("Se agrego exitosamente {} con {} mill de habit.".format(pais, str(nueva_cantidad)))
        print("Muchas gracias por tu aporte...")
    else:
        print("Muchas gracias por tu aporte...")


while True:
    pais = str(input("Que pais quieres consultar: ")).lower()

    try:
        print("La poblacion de {} es de {} millones de habitantes.".format(pais, paises[pais]))
    except KeyError:
        print('No tenemos el dato de la población de {}'.format(pais))
        agregar_pais(pais)
