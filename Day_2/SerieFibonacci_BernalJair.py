def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) <= n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

while True:
    try:
        n = input("Ingrese el valor de 'n' (ingrese 0 para salir): ")
        n = int(n)
        if n != float(n):
            print("Entrada inválida. Por favor, ingrese un número entero.")
        elif n < 0:
            print("Por favor, ingrese un número entero no negativo.")
        elif n == 0:
            break
        else:
            print(fibonacci(n))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
