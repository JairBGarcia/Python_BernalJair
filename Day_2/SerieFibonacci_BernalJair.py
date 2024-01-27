def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) <= n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

while True:
    n = int(input("Ingrese el valor de 'n' (ingrese 0 para salir): "))
    if n == 0:
        break
    else:
        print(fibonacci(n))
