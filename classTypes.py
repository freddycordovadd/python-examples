
"""
Definimos una clase, 
Los metodos en python siempre deben ir con self como primer
parametro para saber q esta siendo referenciado al objeto(clase)
"""


class Persona:
    # Esta es la clase Persona
    # No hay constructor explicito, pero usamos __init__
    def __init__(self,nombre,edad):
        # Se ejecuta al instanciar la clase
        self.Nombre = nombre
        self.Edad = edad

    # Definimos un metodo de la clase Persona
    def mostrar(self):
        print("Nombre: " + self.Nombre)
        print("Edad: " + str(self.Edad))

    # Otro metodo
    def saludar(self):
        print("Hola, yo soy " + self.Nombre)
        

# Creamos una herencia de clase

class Empleado(Persona):
    # Esta es la clase Empleado
    # Aprovechamos el metodo __init__ de la clase padre
    def __init__(self, nombre, edad, salario):
        Persona.__init__(self, nombre, edad)
        self.Salario = salario

    # Metodo que aprovecha el metodo Persona.mostrar
    def mostrar_empleado(self):
        Persona.mostrar(self)
        print("Salario: " + str(self.Salario))

    # Override a un metodo de la clase padre
    def saludar(self):
        print("Hola, soy el empleado " + self.Nombre)


# Instanciamos a la clase Persona

persona1 = Persona("David", 25)
persona1.mostrar()
persona1.saludar()
print("-"*20)

# Creamos otra instancia

persona2 = Persona("Jennifer", 21)
persona2.mostrar()
persona2.saludar()
print("-"*20)

# Probamos la clase con herencia

empleado1 = Empleado("Pedro", 35, 2500)
empleado1.mostrar_empleado()
empleado1.saludar()


