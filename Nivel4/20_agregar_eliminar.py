frutas = [] #declarar una lista de frutas
while True:
    add_delete = input("Agregar (A) / Eliminar (E) / Salir (S): ").upper()
    if add_delete == "A":
        while True:
            fruta_agregar = input("Ingresa una fruta: ")
            if fruta_agregar != "0":
                frutas.append(fruta_agregar)
                print("Para salir escribe 0")
            else:
                break
    elif add_delete == "E":
        while True:
            fruta_borrar = input("Ingresar la fruta que desea eliminar: ")
            if fruta_borrar != "0":
                frutas.remove(fruta_borrar)
                print("Para salir escribe 0")
            else:
                break
    elif add_delete == "S":
        break
    else:
        print("La opción no existe")

print("-------FRUTAS-----------")
for i in frutas: #Recorrer e imprimir la lista
    print(i)