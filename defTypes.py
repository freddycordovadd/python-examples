"""
tipos de metodos def 
"""

# probando metodos con python

def Mostrar(numero):
    "Esta funcion imprime un numero"
    print(numero)


Mostrar(5)
Mostrar(1)
Mostrar(2)
Mostrar(7)

print("-"*20)


# Este ejm muestra como pasar parametros

def Sumatoria(a,b=4,c=8):
    """Metodo q suma tres numeros, dos parametros opcionales,b=4,c=8
    y uno obligatorio"""
    r=a+b+c
    print(r)

a=int(input("Dame un numero:"))
Sumatoria(a)


#############################################
# usando un keyword para pasar los parametros

def muestraValores(a=1,b=2,c=3):
    "Probando metodos con keywords en parametros"
    print("A es ",a)
    print("B es ",b)
    print("C es ",c)


# invocacion normal
muestraValores(4,8,9)
print("-"*20)

# invocacion con keywords
muestraValores(c=33,a=44,b=88)
print("-"*20)

# invocamos con keywords y usando parametros opcionales
muestraValores(b=999)
print("-"*20)


# numero arbitrario de parametros

def sumatoria(a,*mas):
    suma=a
    if len(mas)>0:
        for n in mas:
            suma=suma+n
    print(suma)

sumatoria(1)
sumatoria(1,2)
sumatoria(1,2,3)
sumatoria(1,2,3,4)
sumatoria(1,2,3,4,5)

print("-"*20)

#uso de return

def Sumatoria(a,*mas):
    suma=a
    if len(mas)>0:
        for n in mas:
            suma=suma+n
    return suma

s=Sumatoria(1)
print(s)
