import random

def juego_adivinanza():
    #Este bucle se ejecuta mientras el usuario quiera seguir jugando
    while True:
        #Generamos un numero secreto aleatorio del 1 al 100
        numero_secreto = random.randint(1, 100)
        #Inicializamos el contador de intentos
        intentos = 0

        print("Bienvenido al juego de adivinación. Tienes 10 intentos para adivinar un número entre 1 y 100.")

        #Este bucle se ejecuta mientras el usuario no haya adivinado el numero y no haya agotado sus intentos
        while intentos < 10:
            try:
                suposicion = int(input("Por favor, ingresa tu suposición: "))
                intentos += 1
                if suposicion < numero_secreto:
                    print("El número secreto es mayor. Te quedan", 10 - intentos, "intentos.")
                elif suposicion > numero_secreto:
                    print("El número secreto es menor. Te quedan", 10 - intentos, "intentos.")
                else:
                    print("¡Felicidades! Has adivinado el número secreto en", intentos, "intentos.")
                    break

            #Si el usuario agota sus intentos sin adivinar el numero, mostramos un mensaje y revelamos el numero secreto
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
        else:
            print("Lo siento, has agotado tus intentos. El número secreto era", numero_secreto, ".")

        #Preguntamos al usuario si quiere jugar de nuevo
        jugar_de_nuevo = ""
        while jugar_de_nuevo.lower() not in ["sí", "si", "no"]:
            jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ")
        #Si el usuario no quiere jugar de nuevo, salimos del bucle y terminamos el programa
        if jugar_de_nuevo.lower() not in ["sí", "si"]:
            break
#Llamamos la funcion para iniciar el juego
juego_adivinanza()



