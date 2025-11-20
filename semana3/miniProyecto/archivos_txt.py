from servicios import validate_empty_inventory

    
def save_txt(nombre):
    with open(nombre, 'w') as file:
        file.write("name,price,amount\n")
       
            
def write_line(nombre, inventario):
    with open(nombre , 'a') as file:
         for i in inventario:
            print(i)
            line = f"{i["name"]}, {i["price"]}, {i["amount"]}\n"
            file.write(line)