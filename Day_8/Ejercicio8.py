import json

with open("labuena.json", "r") as f:
    lista = json.load(f)

nombres = []

# Recorrer la lista de clientes y filtrar los que tienen un nombre que empieza por A y termina por n o que empieza por P
for cliente in lista["ventas"]["clientes"]:
    nombre = cliente["nombre"]
    if nombre.startswith("A") and nombre.endswith("n") or nombre.startswith("P"):
        # Añadir el nombre a la lista de nombres
        nombres.append(nombre)

# Ordenar la lista de nombres alfabéticamente
nombres.sort()

# Imprimir el listado de nombres
print("Los nombres de los clientes que empiezan por A y terminan por n y también los nombres que empiezan por P son:")
for nombre in nombres:
    print(nombre)
