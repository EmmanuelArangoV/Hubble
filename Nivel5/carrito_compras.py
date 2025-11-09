carrito = {}

def agregarProducto():
    
    print("\n-- AGREGAR PRODUCTO --")

    producto = input("\nIngresa el producto que quieres agregar -> ")


    precio = input("Ingresa el precio -> ")

    while not precio.isnumeric():
        print("Incorrecto, ingresa un precio")
        precio = input("Ingresa el precio -> ")


    cantidad = input("Ingresa la cantidad -> ")

    while not cantidad.isnumeric():
        print("Incorrecto, ingresa solo numeros")
        cantidad = input("Ingresa la cantidad -> ")
        print("---"*15)

    carrito[producto]={
        "Precio": precio,
        "Cantidad": cantidad
    }

    for producto, info in carrito.items():
        print(f"\nProducto: {producto}\nPrecio: {info['Precio']}\nCantidad: {info['Cantidad']}")
        break


def eliminarProducto():

    print("\n-- ELIMINAR PRODUCTO --")

    if not carrito:
        print("\nNo hay productos")
        return

    producto = input("\nIngrese el producto a eliminar -> ")

    if producto in carrito:

        carrito.pop(producto)
        print("\nse borro producto")
    for producto, info in carrito.items():
        print(f"\nProducto: {producto}\nPrecio: {info['Precio']}\nCantidad: {info['Cantidad']}")

    else:
        print("\nNo existe")

def mostrarProductos():

    print("---"*15)
    print("\n--- TUS PRODUCTOS ---")

    if not carrito:
        print("\nNo hay productos agregados")
        return
    
    for producto, info in carrito.items():
        print(f"\nProducto: {producto}\nPrecio: {info['Precio']}\nCantidad: {info['Cantidad']}")
        print("---"*15)

def totalCarrito():

    print("\n--- TOTAL DE PRODUCTOS  ---")

    if not carrito:
        print("\nNo haz ingresado productos")
        return

    else:
        total = 0

        for x in carrito.values():
            precio = float(x['Precio'])
            cantidad = int(x['Cantidad'])

            total += precio*cantidad

        print(f"Total: {total}")


constante = True

while constante:

    print("\n--- TIENDA DE ROPA ---\n")

    print("-- OPCIONES ---\n")

    print("1. Agregar una producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Total del carrito")
    print("5. Salir")
    print("---"*15)

    opciones = input("\nEscoge una opcion -> ")

    match (opciones):
        case "1":
            agregarProducto()
        case "2":
            eliminarProducto()
        case "3":
            mostrarProductos()
        case "4":
            totalCarrito()
        case "5":
            break
        case _:
            print("Opcion incorrecta")






