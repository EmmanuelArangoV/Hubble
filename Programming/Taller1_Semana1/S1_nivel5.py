print()
print()
print("EJERCICIO: SISTEMAS DE CALIFICACION")
##Se usan condicionales para clasificar las notas y se usa bucle en caso de que el usuario no cumpla la condicion, continue en caso de que si, y break para terminar el programa#
while True:
    try:
        matematicas = float(input("Ingrese la calificacion de matematicas: "))
        ciencias = float(input("Ingrese la calificacion de ciencias: "))
        literatura = float(input("Ingrese la calificacion de literatura: "))
        if matematicas < 0 or matematicas > 5 or ciencias < 0 or ciencias > 5 or literatura < 0 or literatura > 5:
            print("Las calificaciones deben estar entre 0 y 5. Intente de nuevo")
            continue
        promedio = (matematicas + ciencias + literatura) / 3
        if promedio >= 4.5:
            print(f"Calificacion final: {promedio:.2f} - Excelente, sigue asi")
        elif promedio >= 3.5:
            print(f"Calificacion final: {promedio:.2f} - Pasaste pero eres mediocre, debes mejorar")
        else:
            print(f"Calificacion final: {promedio:.2f} - Reprobaste, ¿What do you doing?")
        break           
    except ValueError:
        print("Ingresa solo numeros y que el rango sea de 0 a 5. Intente de nuevo")

print()
print()
print("EJERCICIO: CARRITO DE COMPRAS")
carrito = []
#Se crea lista vacia, y bucle y continue por si el usuario desea agregar algo mas al carrito con el metodo append#
while True:
    try:
        producto = input("Ingrese el nombre del producto para agregar al carrito: ")
        carrito.append(producto)
        print(f"Productos en el carrito: {carrito}")
        agregar = input("¿Desea agregar otro producto? (si/no): ").lower()
        if agregar == 'si':
            continue
        elif agregar == 'no':
            print(f"Productos finales en el carrito: {carrito}")
            
            while True:
                eliminar = input("¿Desea eliminar algun producto del carrito? (si/no): ").lower()
                if eliminar == 'si':
                    producto_eliminar = input("Ingrese el nombre del producto que desea eliminar del carrito: ")
                    if producto_eliminar in carrito:
                        carrito.remove(producto_eliminar)
                        print(f"Producto {producto_eliminar} eliminado. Productos actuales en el carrito: {carrito}")
                    else:
                        print(f"El producto {producto_eliminar} no se encuentra en el carrito.")
                    
                elif eliminar == 'no':
                    print("Carrito actualizado.")
                    print(f"Productos finales en el carrito: {carrito}")
                    break
            break
    
    except ValueError:
        print("Error en la entrada, intente de nuevo.")

print()
print()
print("EJERCICIO: AGENDA DE CONTACTOS")
#Se crea diccionario vacio, y bucle y continue si el usuario desea agregar otro contacto con metodo items y asignacion clave valor#                                                                             metodo append#
agenda = {}
while True:
    try:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el numero de telefono del contacto: ")
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado con numero {telefono}.")
        agregar = input("¿Desea agregar otro contacto? (si/no): ").lower()
        if agregar == 'si':
            continue
        elif agregar == 'no':
            print("Contactos en la agenda:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
            break
    except ValueError:
        print("Error en la entrada, intente de nuevo.")