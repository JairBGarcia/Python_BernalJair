import json

with open("labuena.json", "r") as f:
  ventas = json.load(f)

pedidos = ventas["ventas"]["pedidos"]

pedidos_filtrados = []

for p in pedidos:
  # Comprobamos si el pedido tiene una fecha que empiece por "2017" y un total mayor que 500 con una condición if
  if p["fecha"].startswith("2017") and p["total"] > 500:
    # Si el pedido cumple, lo añadimos a la lista de pedidos filtrados
    pedidos_filtrados.append(p)

#Se imprime el listado de pedidos filtrados
print("Listado de pedidos del año 2017 con total mayor que 500:")
for pedido in pedidos_filtrados:
  print(f" Total: {pedido['total']}, Fecha: {pedido['fecha']}")
