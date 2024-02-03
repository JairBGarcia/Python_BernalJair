##-------------------
##----Ejercicio 1----
##-------------------

#Impresion en consola
print("Hola mundo")

#----Datos Primitivos----

#1.String
texto="Campus"
print(texto)
print(type(texto))

#2.Int
numEnt=1
print(numEnt)

#3.Float
numDec=3.1
print(numDec)

#4.Double
numDeclar=3.13443321
print(numDeclar)

#5.Boolean
boolean = True
print(boolean)

#----Entradas parte del usuario----
entradaUsu = input("Ingrese tu nombre")
print("Tu nombre es: ",entradaUsu)
#----Entradas parte del usuario con definicion de tipo de datos primitivos----
entradaUsunumer = input("Ingrese tu edad")
numerofinal = int(entradaUsunumer)
print("Tu edad es: ",entradaUsunumer)

#----Ciclos----

#1.Ciclo for
for i in range(5): #for contador in range(desde, hasta, pasos):
    print(i)

#2.Ciclo While
booleanito = True
while booleanito == True: #while condicion_a_cumplir
    print("Sigo vivo")

#----Condicional----
texto1 = "Campus"
if texto1 == "Campus":
    print("Soy Campus")
else:
    print("No soy Campus")


#----Funciones----

#1.Arguments

def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old")
    print("Happy birthday to you")
    print()

happy_birthday("bro", 20)
happy_birthday("steve", 30)
happy_birthday("joe", 40)

#2.Return

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def div(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(div(1, 2))

#----Arreglos----

#1.List
# [] ordenado y modificable. Duplicados OK
fruits = ["apple", "orange", "banana", "coconut"]

#2.Set
#{} desordenado e inmutable, pero Agregar o quitar está bien. NO duplicados
fruits = {"apple", "orange", "banana", "coconut"}

#3.Tuple
#() ordenado e inmutable. Duplicados OK. MÁS RÁPIDO
fruits = ("apple", "orange", "banana", "coconut")


## Desarrollado por JAIR ANDRES BERNAL GARCIA - 1098607050