import csv

fieldnames= ["name", "price", "amount"]

def create_csv(ruta_csv, inventario):
    with open(ruta_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        
def add_registro(ruta_csv,inventario):
    with open(ruta_csv, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerows(inventario)
        
def load_register(ruta_csv):
    with open(ruta_csv, 'r', newline='') as file:
        reader_csv = csv.DictReader(file)
        encabezados = reader_csv.fieldnames
        registros = list(reader_csv)
        return registros, encabezados
    
def print_data(ruta_csv):
    data = load_register(ruta_csv)
    for fila in data:
        print(f"{fila["name"]:<15}|{fila["price"]:<10}|{fila["amount"]:<10}")

def fusionar_datos(ruta_user,ruta_csv):
    datos_user = load_register(ruta_user)
    datos = load_register(ruta_csv)
    combinados = []
    print(datos_user[1])
    if not datos_user[1] == datos[1]:
        return"\033[31mEncabezados diferentes\033[0m"
    else:
        combinados = datos[0] + datos_user[0]
        with open(ruta_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows(combinados)
        print(combinados)
        return "\033[32mArchivos csv fusionados\033[0m"
    
def existe_en_csv(datos_existentes, nuevos_datos):
    for i,dato in enumerate(nuevos_datos):
        if dato[0] == datos_existentes[i][0]:
            print("existe")
            print(dato)
        else:
            print("no existe")
        

    