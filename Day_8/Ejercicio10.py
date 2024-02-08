
import json

with open("labuena.json", "r") as f:
    lista = json.load(f)

nombres_ruiz = set()
# Recorrer la lista de comerciales y filtrar los que tienen como apellido "Ruiz"
for comercial in lista["ventas"]["comerciales"]:
    if comercial["apellido1"] == "Ruiz" or comercial["apellido2"] == "Ruiz":
        # Añadir el nombre del comercial al conjunto
        nombres_ruiz.add(comercial["nombre"])

# Convertir el conjunto en una lista y ordenarla alfabéticamente
nombres_ruiz = sorted(list(nombres_ruiz))

# Imprimir el listado de nombres
print("Los nombres de los comerciales que tienen como apellido 'Ruiz' son:")
for nombre in nombres_ruiz:
    print(nombre)
