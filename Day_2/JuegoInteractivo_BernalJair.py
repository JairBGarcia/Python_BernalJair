import random

def juego_adivinanza():
    while True:
        numero_secreto = random.randint(1, 100)
        intentos = 0

        print("Bienvenido al juego de adivinación. Tienes 10 intentos para adivinar un número entre 1 y 100.")

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
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
        else:
            print("Lo siento, has agotado tus intentos. El número secreto era", numero_secreto, ".")

        jugar_de_nuevo = ""
        while jugar_de_nuevo.lower() not in ["sí", "si", "no"]:
            jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ")
        if jugar_de_nuevo.lower() not in ["sí", "si"]:
            break

juego_adivinanza()



