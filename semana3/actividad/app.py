from crud import CRUD

crud = CRUD()
archivo = "datos.csv"
crud.crear_archivo(archivo)

while True:
    print("----MENU----")
    print("1.Crear persona")
    print("2.Listar Personas")
    print("3.Eliminar")
    print("4.Salir")

    opcion = input("ingresar una opcion: ")

    if opcion == "1":
        nombre = input("Ingresar Nombre: ")
        edad = input("Ingresar edad: ")
        id_creado = crud.crear(archivo, nombre, edad)
        print(f"Persona creada con Id -> {id_creado}")

    elif opcion == "2":
        datos = crud.listar(archivo)
        for dato in datos:
            print(f"ID: {dato[0]}| Nombre: {dato[1]}| Edad: {dato[2]}")
    
    elif opcion == "3":
        print("Eliminar")
        id_eliminar = input("Que ID desea eliminar?: ")
        crud.eliminar_por_id(archivo, id_eliminar)

    elif opcion == "4":
        print("Saliendo")
        break
    else:
        print("opcion no existe")