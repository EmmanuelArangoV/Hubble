import json

def create_json(nombre, inventario):
    with open(nombre, 'w') as file:
        json.dump(inventario, file, indent=4)
        