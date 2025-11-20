import csv

def create_csv(nombre, inventario):
    with open(nombre, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(inventario[0].keys())
        
def add_registro(nombre,inventario):
    with open(nombre, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=inventario[0].keys())
        writer.writerows(inventario)
        
def load_register(nombre):
    with open(nombre, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return reader
    
def print_data(nombre):
    load_register(nombre)
    