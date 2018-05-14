import random

# Todos los posibles caracteres
x = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM0123456789=)(/&%$!"


def crear_password(respuesta):
    """
    Crea una password debil, media o fuerte
    segun la opcion del usuario
    """
    if respuesta == 0:
        return "".join(random.sample(x, 6))
    elif respuesta == 1:
        return "".join(random.sample(x, 9))
    else:
        return "".join(random.sample(x, 12))


print("Que tan fuerte quieres tu password??")
print("-"*10)
print("Escribe 0 para Debil")
print("Escribe 1 para Media")
print("Escribe 2 para Fuerte")
print("-"*10)
respuesta = int(input("Escribe tu respuesta: "))


print("-"*20)
if respuesta == 0:
    print("Escogiste password Debil de 6 caracteres.")
elif respuesta == 0:
    print("Escogiste password Media de 9 caracteres.")
else:
    print("Escogiste password Fuerte de 12 caracteres.")

password = crear_password(respuesta)
print("Tu password es: " + password)
