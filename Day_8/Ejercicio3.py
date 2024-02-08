import json

miVariable = open("labuena.json", "r")
miJson = json.load(miVariable)

clientes = set()
# Recorremos la lista de pedidos del diccionario
for pedido in miJson["ventas"]["pedidos"]:
    # Añadimos el identificador del cliente a el conjunto
    clientes.add(pedido["id_cliente"])
print(clientes)
