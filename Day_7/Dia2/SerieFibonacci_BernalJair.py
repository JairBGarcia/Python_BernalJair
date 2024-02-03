def fibonacci(n):
    #Inicializamos la secuencia con los dos primeros terminos de la secuencia de fibonaccion
    secuencia = [0, 1]
    #Mientras la longitud de la secuencia sea menor o igual a n
    while len(secuencia) <= n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia
#Bucle infinito que se ejecuta hasta que el usuario decida salir
while True:
    try:
        n = input("Ingrese el valor de 'n' (ingrese 0 para salir): ")
        n = int(n)

        #Si n no es un numero entero, mostramos un mensaje de error
        if n != float(n):
            print("Entrada inválida. Por favor, ingrese un número entero.")
        #Si n es un numero negativo, mostramos un mensaje de error
        elif n < 0:
            print("Por favor, ingrese un número entero no negativo.")
        #Si n es igual a 0, salimos del bucle y terminamos el programa
        elif n == 0:
            break
        #Si n es un numero entero no negativo distinto de 0, generamos la secuencia de Fibonnaci hasta el termino n y la imprimimos
        else:
            print(fibonacci(n))
        #SI la entrada del usuario no puede ser convertida a un numero entero, mostramos un mensaje de error
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
