import json

with open("labuena.json", "r") as f:
    lista = json.load(f)

nombres = []
# Recorrer la lista de comerciales y filtrar los que tienen una comisión entre 0.05 y 0.11
for comercial in lista["ventas"]["comerciales"]:
    if 0.05 <= comercial["comision"] <= 0.11:
        # Concatenar el nombre y los apellidos del comercial
        nombre_completo = comercial["nombre"] + " " + comercial["apellido1"] + " " + comercial["apellido2"]
        # Añadir el nombre completo a la lista de nombres
        nombres.append(nombre_completo)

# Imprimir el listado de nombres
print("Los comerciales que tienen una comisión entre 0.05 y 0.11 son:")
for nombre in nombres:
    print(nombre)
