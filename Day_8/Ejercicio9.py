import json

with open("labuena.json", "r") as f:
    lista = json.load(f)

nombres_a = []

# Recorrer la lista de clientes y filtrar los que tienen un nombre que empieza por A
for cliente in lista["ventas"]["clientes"]:
    nombre = cliente["nombre"]
    if nombre.startswith("A"):
        # Añadir el nombre a la lista de nombres
        nombres_a.append(nombre)

# Ordenar la lista de nombres alfabéticamente
nombres_a.sort()

# Imprimir el listado de nombres
print("Los nombres de los clientes que empiezan por A son:")
for nombre in nombres_a:
    print(nombre)
