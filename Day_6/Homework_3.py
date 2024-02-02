class bolita:
    #El método __init__ en Python se utiliza para inicializar una clase y sus atributos
    def __init__(self, x, y, z, radio):
        self.x = x
        self.y = y
        self.z = z
        self.radio = radio

def ball_collide(bola1, bola2):
    # Calcular la distancia entre las dos bolas
    distance = ((bola2.x - bola1.x)**2 + (bola2.y - bola1.y)**2 + (bola2.z - bola1.z)**2)**0.5

    # Las bolas están colisionando si la distancia es menor o igual a la suma de sus radios
    return distance <= bola1.radio + bola2.radio

def get_ball():
    x = float(input("Introduce la coordenada x del centro de la bola: "))
    y = float(input("Introduce la coordenada y del centro de la bola: "))
    z = float(input("Introduce la coordenada z del centro de la bola: "))
    radio = float(input("Introduce el radio de la bola: "))
    return bolita(x, y, z, radio)

# Solicitar al usuario que introduzca los detalles de las bolas
print("Introduce los detalles de la primera bolita")
bola1 = get_ball()
print("Introduce los detalles de la segunda bolita")
bola2 = get_ball()

# Verificar si las bolas están colisionando
if ball_collide(bola1, bola2):
    print(True)
else:
    print(False)
