product_list = []

def CreateProduct():
    product = {}
    while True: #validar el nombre del producto
        try:
            name_prod = input("Ingresar nombre del producto: ")
            break
        except ValueError:
            print("Ingresa un valor válido para este campo")


    while True: #validar el precio del producto
        try:
            price_product = float(input("Ingresar valor del producto: "))
            if price_product > 0:
                break
            else:
                print("ingresar valor mayor a 0")
        except ValueError:
            print("Ingresa un valor válido para este campo")

    while True: #validar la cantidad del producto
        try:
            amount_products = int(input("Ingresar cantidad de productos: "))
            if amount_products > 0:
                break
            else:
                print("ingresar valor mayor a 0")
        except ValueError:
            print("Ingresa un valor válido para este campo")

    product["name"] = name_prod
    product["price"] = price_product
    product["amount"] = amount_products

    return product

def ShowInfo(products_list):
    if len(products_list) == 0:
        print("\033[31mInventario vacío, Agrega productos para visualizarlos\033[0m")
    else:
        for product in products_list:
            print(f"Producto: {product["name"]} | Precio: {product["price"]}  | Cantidad: {product["amount"]}")

def CalculateStats(products_list):
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
        
    print(f"{'Totales':<15}|{'':<10}|{sum_products:<10}|{total:<10}")

while True:
    try:
        res = int(input("¿Qué deseas hacer? \n1-Agregar producto \n2-Mostrar Inventario \n3-Calcular estadísticas \n0-Salir \n---> "))
        match res:
            case 1:
                product_list.append(CreateProduct())
            case 2:
                ShowInfo(product_list)
            case 3:
                CalculateStats(product_list)
            case 0:
                break
            case _:
                print('\033[31mOpción no válida\033[0m')
    except ValueError:
        print("\033[31mIngresa un valor válido\033[0m")
        
