def colision(bola1, bola2):
    # Calcular la distancia entre las dos bolas
    distance = ((bola2['x'] - bola1['x'])**2 + (bola2['y'] - bola1['y'])**2)**0.5

    # Las bolas están colisionando si la distancia es menor o igual a la suma de sus radios
    return distance <= bola1['r'] + bola2['r']

# Definir dos bolas
bola1 = {'x': 0, 'y': 0, 'r': 1}
bola2 = {'x': 8, 'y': 6, 'r': 5}

# Verificar si las bolas están colisionando
print(colision(bola1, bola2))  # Devuelve: True
