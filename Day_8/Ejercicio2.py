import json

with open("labuena.json", "r") as f:
  ventas = json.load(f)

pedidos = ventas["ventas"]["pedidos"]

pedidos_ordenados = sorted(pedidos, key=lambda p: p["total"], reverse=True)

pedidos_mayores = pedidos_ordenados[:2]

print("Los dos pedidos de mayor valor son:")
for pedido in pedidos_mayores:
  print(f"Total: {pedido['total']},ID Cliente: {pedido['id_cliente']}")
