import json

with open("labuena.json", "r") as f:
    data = json.load(f)
    comerciales = data["ventas"]["comerciales"]

max_comision = 0

for comercial in comerciales:
    comision = comercial["comision"]
    if comision > max_comision:
        max_comision = comision

print(f"El valor máximo de la comisión es {max_comision}")
