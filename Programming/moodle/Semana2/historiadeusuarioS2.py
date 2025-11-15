print()
print("Validacion de datos con condicionales \n")
inventario = []
print("¿Que accion desea realizar?\n")
print("==>1. Agregar producto")
print("==>2. Mostrar inventario")
print("==>3. Calcular estadistica")
print("==>4. Salir \n")

def agregar_producto(inventario):
    while True:
        nombre = input("\nEscojiste agregar producto, por favor ingresa tu producto: ").lower()
        precio = float(input("Ingresa el precio del producto: $"))
        cantidad = int(input("Ingresa la cantidad del producto: "))
        inventario.append({
        "nombre" : nombre, 
        "precio" : precio, 
        "cantidad" : cantidad
        })
        mas_agg = input(f"\nAgregaste {nombre}, ¿desea agregar otro producto? si/no: ").lower()
        if mas_agg == "si":
            continue 
        else:
            break

def mostrar_inventario(inventario):
    mostrar = input(f"\nEscojiste mostrar inventario, acontinuacion veras tu inventario: \n").lower()
    if len(inventario) != 0:
        for producto in inventario:
            print(f"Producto: {producto["nombre"]:<15} | Precio: ${producto["precio"]:<15} | Cantidad: {producto["cantidad"]:<15}")
    else:
        print("El inventario esta vacio")

def calcular_total(inventario):
        estadistica = input("\nEscojiste mostrar estadistica, acontinuacion te mostrare la estadistica: ")
        total = 0
        for item in inventario:
            total += item["precio"] * item["cantidad"]
        print(f"\nEl total de lo que tienes en tu inventario es: ${total}")

while True:
    opcion = input("\nDigita el numero de tu opcion: ")
    if opcion == "1":
        agregar_producto(inventario)
        
    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        calcular_total(inventario)
    
    elif opcion == "4":
        confirmacion = input("¿Esta seguro de salir del sistema?: si/no: ")
        if confirmacion == "si":
            print("Saliendo del sistema")
            break
        else:
            print("Volviendo al sistema")
                
    else:
        print("==>Digita una opcion que este en el rango de 1-4<==")