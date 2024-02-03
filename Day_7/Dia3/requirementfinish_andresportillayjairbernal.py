contador=0;dividir = lambda n: (n // 10, *divmod(n % 10, 5)); numero = int(input("")); monedas_10, monedas_5, monedas_1 = dividir(numero);suma = "".join(["10+"*monedas_10,"5"*monedas_5,"+1"*monedas_1]);contador+= monedas_10+monedas_5+monedas_1;print(f"{contador}");print(f"{suma} ")


"""
---------lambda--------------
Funcion lambda o mas conocida como funcion anonima nos permite crear funciones mas cortas y resumidaas
Ejemplo: 
def suma(n1,n2):
    a=n1+n2
    return(a)
print(suma(5,2))
# Cuando simplemente con lambda se podria hacer
suma = lambda n1, n2: n1 + n2;print(suma(5, 2))
-----------Division de piso--------------------
la division de piso o // nos permite que cuando se relize una division entre dos numeros nos 
entregue el conciente entero (redondea hacia abajo)
Ejemplo:
             42/10=4,2---->42//10=4
--------------------DivMod-------------------------
La funcion divmod
   Nos sirve para que nos entregue el valor del consciente y el residuo respectivamente
   ejemplo: DivMod(9,2)
   Nos imprimiria los valores de 4 y 1
----------------------------------------------------
Luego se almacenan variables en su orden respectivo
---------------------------------------------------
Este método toma una lista (o cualquier iterable) de cadenas de texto y las une en una sola cadena. El carácter o los caracteres que se usan para unir las cadenas se especifican antes de .join
un ejemplo
ista_de_palabras = ['Hola', 'mundo', 'Python']
frase = ' '.join(lista_de_palabras)
y pues lo que hace el join es unir las palabras en una sola cadena
en el ejemplo pues al momento de imprimir une lo que esta en la lista como dice su definicion y lo que imprime de salida sera hola mundo python
lit lo que hace el join es unir las palabras en un solo mensaje de impresion y pues usa un espacio entre comillas como se ve al principio de frase para separar o crear los espacios
lo mismo pasa en el ejercicio donde si usted observa despues de la vairable suma los "" es para crear el espacio en cada una de las operaciones
y si no ponemos esos "" python dara error debido a que esas entrecomillas son las que usan el metodo para unir todo en cadena   
"""

