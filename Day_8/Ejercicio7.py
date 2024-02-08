import json

with open("labuena.json", "r") as f:
    lista = json.load(f)

sevilla = []
# Recorrer la lista de clientes y filtrar los que tienen la ciudad "Sevilla"
for cliente in lista["ventas"]["clientes"]:
    if cliente["ciudad"] == "Sevilla":
        # Crear un diccionario con el identificador, nombre y primer apellido del cliente
        datos = {"id": cliente["id"], "nombre": cliente["nombre"], "apellido1": cliente["apellido1"]}
        # Añadir el diccionario a la lista de Sevilla
        sevilla.append(datos)

# Ordenar la lista de Sevilla alfabéticamente por apellidos y nombre
sevilla.sort(key=lambda x: (x["apellido1"], x["nombre"]))

# Imprimir el listado de Sevilla
print("Los clientes de Sevilla son:")
for datos in sevilla:
    print(datos["id"], datos["nombre"], datos["apellido1"])
