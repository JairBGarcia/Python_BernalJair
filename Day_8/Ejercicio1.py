import json

with open("labuena.json", "r") as f:
  ventas = json.load(f)

pedidos = ventas["ventas"]["pedidos"]

# Ordenamos la lista de pedidos por fecha, de más reciente a más antiguo
pedidos_ordenados = sorted(pedidos, key=lambda p: p["fecha"], reverse=True)

# Imprimimos el listado de pedidos
print("Listado de pedidos ordenados por fecha:")
for pedido in pedidos_ordenados:
  print(f" Fecha: {pedido['fecha']}, ID Cliente: {pedido['id_cliente']}")
