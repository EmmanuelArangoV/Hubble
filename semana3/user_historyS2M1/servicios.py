
def validar_entradas(tipo, prompt, validacion_extra = None):
    mesajes = {
        int : "Ingresar un número y que sea mayor a 0",
        float: "Ingresar un número y que sea mayor a 0",
        str : "No ingresar un texto vacío"
    }
    while True:
        try:
            valor = tipo(input(prompt))
            if validacion_extra and not validacion_extra(valor):
                print(f"\033[31m{mesajes[tipo]}\033[0m")
                continue    
            return valor
        except ValueError:
            print(f"\033[31m{mesajes[tipo]}\033[0m")
    
def create_product():
    product = {}
    
    #solicitar 
    name_prod = validar_entradas(str, "Ingresar nombre del producto: ", lambda x:len(x) > 0)
    
    price_product = validar_entradas(float, "Ingresar valor del producto: ", lambda x : x>0)

    amount_products = validar_entradas(int, "Ingresar cantidad de productos: ", lambda x:x>0)

    product["name"] = name_prod
    product["price"] = price_product
    product["amount"] = amount_products

    return product

def show_inventory(products_list):
    if len(products_list) == 0:
        print("\033[31mInventario vacío, Agrega productos para visualizarlos\033[0m")
    else:
        for product in products_list:
            print(f"Producto: {product["name"]} | Precio: {product["price"]}  | Cantidad: {product["amount"]}")

def calculate_stats(products_list):
    total = 0
    sum_total = 0
    sum_products = 0
    print("--------------------------------------------------------------------------------------------")
    print(f"{'Producto':<15}|{'Precio':<10}|{'cantidad':<10}|{'Total':<10}")
    for product in products_list:
        total = product["price"]*product["amount"]
        sum_total += total
        sum_products += product["amount"]
        print("--------------------------------------------------------------------------------------------")
        print(f"{product["name"]:<15}|{product["price"]:<10}|{product["amount"]:<10}|{total:<10}")
        print("--------------------------------------------------------------------------------------------")
        
    print(f"{'Totales':<15}|{'':<10}|{sum_products:<10}|{sum_total:<10}\n")
    