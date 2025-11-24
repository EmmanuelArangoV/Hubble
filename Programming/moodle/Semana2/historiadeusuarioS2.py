print()
print("Validacion de datos con condicionales \n")
# Lista vacía para almacenar los productos del inventario
inventario = []

# Mostrar el menú de opciones al usuario
print("¿Que accion desea realizar?\n")
print("==>1. Agregar producto")
print("==>2. Mostrar inventario")
print("==>3. Calcular estadistica")
print("==>4. Salir \n")

# Función para agregar productos al inventario
def agregar_producto(inventario):
    while True:
        # Solicitar datos del producto al usuario
        nombre = input("\nEscojiste agregar producto, por favor ingresa tu producto: ").lower()
        precio = float(input("Ingresa el precio del producto: $"))
        cantidad = int(input("Ingresa la cantidad del producto: "))
        
        # Agregar producto como diccionario a la lista inventario
        inventario.append({
        "nombre" : nombre, 
        "precio" : precio, 
        "cantidad" : cantidad
        })
        
        # Preguntar si desea agregar otro producto
        mas_agg = input(f"\nAgregaste {nombre}, ¿desea agregar otro producto? si/no: ").lower()
        if mas_agg == "si":
            continue  # Continuar el ciclo while
        else:
            break    # Salir del ciclo while

# Función para mostrar todos los productos del inventario
def mostrar_inventario(inventario):
    mostrar = input(f"\nEscojiste mostrar inventario, acontinuacion veras tu inventario: \n").lower()
    
    # Verificar si el inventario tiene productos
    if len(inventario) != 0:
        # Recorrer cada producto y mostrar sus detalles
        for producto in inventario:
            print(f"Producto: {producto["nombre"]:<15} | Precio: ${producto["precio"]:<15} | Cantidad: {producto["cantidad"]:<15}")
    else:
        print("El inventario esta vacio")  # Mensaje si el inventario está vacío

# Función para calcular el valor total del inventario
def calcular_total(inventario):
        estadistica = input("\nEscojiste mostrar estadistica, acontinuacion te mostrare la estadistica: ")
        total = 0
        
        # Calcular el valor total (precio * cantidad) de cada producto
        for item in inventario:
            total += item["precio"] * item["cantidad"]
            
        # Mostrar el valor total del inventario
        print(f"\nEl total de lo que tienes en tu inventario es: ${total}")

# Ciclo principal del programa
while True:
    # Solicitar opción al usuario
    opcion = input("\nDigita el numero de tu opcion: ")
    
    # Opción 1: Agregar producto
    if opcion == "1":
        agregar_producto(inventario)
        
    # Opción 2: Mostrar inventario
    elif opcion == "2":
        mostrar_inventario(inventario)

    # Opción 3: Calcular estadísticas
    elif opcion == "3":
        calcular_total(inventario)
    
    # Opción 4: Salir del sistema
    elif opcion == "4":
        # Confirmar si realmente desea salir
        confirmacion = input("¿Esta seguro de salir del sistema?: si/no: ")
        if confirmacion == "si":
            print("Saliendo del sistema")
            break  # Terminar el ciclo while y salir del programa
        else:
            print("Volviendo al sistema")  # Continuar en el programa
                
    # Manejar opciones inválidas
    else:
        print("==>Digita una opcion que este en el rango de 1-4<==")