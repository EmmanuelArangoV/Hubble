import json

def create_json(nombre, inventario):
    with open(nombre, 'w') as file:
        json.dump(inventario, file, indent=4)
        
def load_json(nombre):
    with open(nombre, 'r') as file:
        datos = json.load(file)
        
    return datos

def agregar_data(nombre , inventario):
    datos = load_json(nombre)
    with open(nombre,'w') as file:
        json.dump(datos+inventario, file, indent=4)         