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

## Desarrollado por JAIR ANDRES BERNAL GARCIA - 1098607050