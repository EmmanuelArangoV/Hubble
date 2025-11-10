# while True:
#     try:
#         res = int(input("¿Qué deseas hacer? \n1-Agregar producto \n2-Mostrar Inventario \n3-Calcular estadísticas \n0-Salir \n---> "))
#         match res:
#             case 1:
#                 print('Agregar')
#             case 2:
#                 print('Mostrar')
#             case 3:
#                 print('Calcular')
#             case 0:
#                 break
#             case _:
#                 print('Opción no válida')
#     except ValueError:
#         print("Ingresa un valor válido")
        
                
def create_product():
    product = {}
    while True:
        try:
            name_prod = input("Ingresar nombre del producto: ")
            price_product = input(float("Ingresar valor del producto"))
            amount_products = input(int("Ingresar cantidad de productos"))
        except ValueError:
            print("Ingresa un valor válido para este campo")

create_product()
#def agregar_producto():