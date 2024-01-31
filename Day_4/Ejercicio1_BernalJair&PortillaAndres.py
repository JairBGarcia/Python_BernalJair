"""Esta es la función Ejercicio1 que toma tres parámetros: n (la longitud de la lista), k (un número para la operación de módulo),
 y lista (una lista de enteros). Esta función cuenta el número de pares en la lista donde la suma del par es divisible por k"""
def Ejercicio1(n, k, lista):
    contador = 0
    for i in range(n):
        for j in range(i+1, n):
            if (lista[i] + lista[j]) % k == 0:
                contador += 1
    return contador
"""Esta parte del código maneja la entrada y salida del programa. Primero, lee T casos de prueba de la entrada. Para cada caso de prueba, 
lee n y k, y una lista de n enteros. Luego, llama a la función Ejercicio1 con estas entradas e imprime el resultado."""

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split()) 
    lista = list(map(int, input().split()))
    result = Ejercicio1(n, k,lista)
    print(f'Case #{t}: {result}')

"""La función split() en Python es un método que se aplica a las cadenas de texto (strings). 
Esta función divide una cadena en varias subcadenas utilizando un delimitador especificado y devuelve una lista de estas subcadenas
Por ejemplo, si tienes una cadena como “Hola mundo” y usas el espacio " " como delimitador, al usar split() te devuelve una lista que
 tiene [“Hola”, “Mundo”].
 En resumen, split() convierte una cadena en una lista, mientras que join() convierte una lista en una cadena
 
 map(). Esta función toma dos argumentos: una función y un iterable (como una lista o una tupla),map()  Entonces, 
 map(int, input().split()) está convirtiendo cada subcadena en un entero.map(int, input().split()) devuelve un objeto de mapa 
 iterable que contiene los enteros [1, 2, 3]. """
