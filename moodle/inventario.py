#Se pide nombre del producto#
producto = input("Introduce el nombre del producto: ")

#Se pide precio del producto, coloca otro tipo de datos que no sean numericos, le pide que ingrese uno correcto#
while True:
    try:
        precio = float(input("Introduce el precio del producto: $"))
        break
    except ValueError:
        print("Introduce un precio valido, intentalo de nuevo: ")

#Se pide cantidad del producto, si coloca otro tipo de datos que no sean numericos, le pide que ingrese uno correcto#
while True:
    try:
        cantidad = int(input("Introduce la cantidad del producto: "))
        break
    except ValueError:
        print("Introduce una cantidad valida, intentalo de nuevo: ")

#Operacion matematica que determina el costo total de los productos#
costo_total = cantidad * precio


print(f"Producto: {producto} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")




