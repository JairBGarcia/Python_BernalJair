motos = {"yamaha": 20000, "honda": 18000, "suzuki": 17000}

while True:
    # Mostrar las motos disponibles
    print("Motos disponibles: ")
    for moto in motos:
        print("- ", moto)
    
    # Preguntar al usuario por una moto
    moto = input("Por favor, ingresa el nombre de la moto que deseas comprar: ")

    # Verificar si la moto está en el diccionario
    if moto in motos:
        # Preguntar al usuario por la cantidad
        cantidad = int(input("Por favor, ingresa la cantidad que deseas comprar: "))
        
        # Calcular el precio total
        precio_total = motos[moto] * cantidad
        
        # Mostrar el precio total
        print(f"El precio total de {cantidad} {moto} es {precio_total}")
    else:
        # Informar al usuario que la moto no está disponible
        print(f"Lo siento, la moto {moto} no está disponible.")
    
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas comprar otra moto? (s/n): ")
    if continuar.lower() != "s":
        break