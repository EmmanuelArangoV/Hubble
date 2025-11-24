inventario = [
    {"nombre": "Manzana", "precio": 1500, "cantidad": 10},
    {"nombre": "Banana", "precio": 1100, "cantidad": 20},
    {"nombre": "Fresa", "precio": 3000, "cantidad": 15},
    {"nombre": "Pera", "precio": 2800, "cantidad": 12},
    {"nombre": "Uva", "precio": 4000, "cantidad": 8},
    {"nombre": "Tomate", "precio": 1500, "cantidad": 30},
    {"nombre": "Zanahoria", "precio": 1000, "cantidad": 25},
    {"nombre": "Brocoli", "precio": 2300, "cantidad": 10},
    {"nombre": "Espinaca", "precio": 1800, "cantidad": 18},
    {"nombre": "Pepino", "precio": 1200, "cantidad": 22},
    {"nombre": "Arroz", "precio": 3000, "cantidad": 50},
    {"nombre": "Frijoles", "precio": 1000, "cantidad": 40},
    {"nombre": "Lentejas", "precio": 2000, "cantidad": 30},
    {"nombre": "Maiz", "precio": 1100, "cantidad": 35},
    {"nombre": "Arberjas", "precio": 3500, "cantidad": 12}
]

def agregar_producto(inventario):
    """
    Función para agregar productos al inventario.
    Permite agregar múltiples productos hasta que el usuario decida parar.
    """
    while True:
        # Solicitar datos del producto al usuario
        nombre = input("\nEscojiste agregar producto, por favor ingresa tu producto: ").capitalize()
        precio = int(input("Ingresa el precio del producto: $"))
        cantidad = int(input("Ingresa la cantidad del producto: "))
        # Agregar producto al inventario como diccionario
        inventario.append({
            "nombre": nombre, 
            "precio": precio, 
            "cantidad": cantidad
        })
        # Preguntar si desea agregar otro producto
        mas_agg = input(f"\nAgregaste {nombre}, ¿desea agregar otro producto? si/no: ").capitalize()
        if mas_agg == "si":
            continue  # Continuar el ciclo para agregar otro producto
        else:
            break    # Salir del ciclo

def mostrar_inventario(inventario):
    """
    Función para mostrar todo el inventario de productos.
    Muestra formato tabla o mensaje si está vacío.
    """
    print(f"\nEscojiste mostrar inventario, acontinuacion veras tu inventario\n")
    # Verificar si el inventario tiene productos
    if len(inventario) != 0:
        # Recorrer y mostrar cada producto con formato
        for producto in inventario:
            print(f"Producto: {producto['nombre']:<15} | Precio: ${producto['precio']:<15} | Cantidad: {producto['cantidad']:<15}")
    else:
        print("El inventario esta vacio")

def buscar_producto(inventario):
    """
    Función para buscar un producto por nombre en el inventario.
    """
    # Solicitar nombre del producto a buscar
    buscar = input(f"\nEscojiste buscar producto, por favor ingresa tu producto: ").capitalize()
    # Verificar si hay productos en el inventario
    if len(inventario) > 0:
        # Buscar producto en el inventario
        for producto in inventario:
            if producto["nombre"] == buscar:
                print("\nProducto encontrado")
                print(f"Producto: {producto['nombre']:<15}")
                break
        else:
            # Este else corresponde al for (se ejecuta si no hubo break)
            print("\nEste no producto no se encuentra en el inventario. Intenta nuevamente o agrega el producto")
    else:
        print("\nEl inventario esta vacio, no hay productos que buscar")

def actualizar_producto(inventario):
    """
    Función para actualizar precio y cantidad de un producto existente.
    """
    # Solicitar nombre del producto a actualizar
    actualizar = input("\nPor favor ingresa el producto que deseas actualizar: ").capitalize()
    # Verificar si hay productos en el inventario
    if len(inventario) > 0:
        # Buscar producto para actualizar
        for producto in inventario:
            if producto["nombre"] == actualizar:
                # Solicitar nuevos valores
                nuevo_precio = int(input(f"\nIntroduce el nuevo precio del producto {actualizar}: $"))
                nueva_cantidad = int(input(f"Introduce la nueva cantidad del producto {actualizar}: "))
                # Actualizar los valores del producto
                producto.update({"precio": nuevo_precio, "cantidad": nueva_cantidad})
                # Mostrar producto actualizado
                print(f"\nProducto: {producto['nombre']:<15} | Precio: ${producto['precio']:<15} | Cantidad: {producto['cantidad']:<15}")
                break
        else:
            # Producto no encontrado
            print("\nEste no producto no se encuentra en el inventario. Intenta nuevamente o agrega el producto")
    else:
        print("\nEl inventario esta vacio, no hay productos que actualizar")

def eliminar_producto(inventario):
    """
    Función para eliminar un producto del inventario.
    """
    # Solicitar nombre del producto a eliminar
    eliminar = input("\nPor favor ingresa el producto que deseas eliminar: ").capitalize()
    # Verificar si hay productos en el inventario
    if len(inventario) > 0:
        # Buscar producto para eliminar
        for producto in inventario:
            if producto["nombre"] == eliminar:
                # Eliminar producto del inventario
                inventario.remove(producto)
                print(f"\nProducto {eliminar} ha sido eliminado")
                break
        else:
            # Producto no encontrado
            print("\nEste producto no existe en el inventario")
    else:
        print("\nEl inventario esta vacio, no hay productos que eliminar")

def estadisticas(inventario):
    """
    Función para calcular y mostrar estadísticas del inventario.
    Incluye: unidades totales, valor total, producto más caro y producto con mayor stock.
    """
    # Verificar si hay productos en el inventario
    if len(inventario) > 0:
        # Calcular unidades totales (suma de todas las cantidades)
        unidades_totales = sum(producto["cantidad"] for producto in inventario)
        print(f"\nLa cantidad total de todos los productos en el inventario es: {unidades_totales}")
        # Calcular valor total del inventario (precio * cantidad de cada producto)
        valor_total = sum(producto["precio"] * producto["cantidad"] for producto in inventario)
        print(f"\nTu inventario esta valorado en: ${valor_total}")
        # Encontrar el producto más caro (mayor precio)
        producto_mas_caro = max(inventario, key=lambda producto: producto["precio"])
        print(f"\nEl producto mas caro de tu inventario es: {producto_mas_caro['nombre']}\ncon precio de ${producto_mas_caro['precio']}")
        # Encontrar el producto con mayor stock (mayor cantidad)
        producto_mayor_stock = max(inventario, key=lambda producto: producto["cantidad"])
        print(f"\nEl producto con mayor stock de tu inventario es: {producto_mayor_stock['nombre']}\ncon {producto_mayor_stock['cantidad']} unidades")
    else:
        print("\nEl inventario esta vacio, no hay estasdistica que mostrar")