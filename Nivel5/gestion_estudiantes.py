baseDeDatos={}

def crearEstudiante():
    print("---"*15)
    print("\n** Modulo CREAR ESTUDIANTE **\n")

    cedulaID=input("- Ingresa Documento Del Estudiante --> ")

    while cedulaID in baseDeDatos:
        print("\n-> El documento ya Existe, escribe otra")
        print("---"*15)            
        cedulaID=input("- Ingresa Documento Del Estudiante --> ")
            
    while not cedulaID.isnumeric():
        print("---"*15)
        print("\nDato Incorrecto Ingresa Solo Numeros ❌\n")

        cedulaID=input("\n- Ingresa Documento  Del Estudiante --> ")

    nombre=input("- Ingresa Nombre Del Estudiante --> ")

    while not nombre.isalpha():
        print("---"*15)
        print("\nNombre Invalido ❌\n")
        nombre=input("- Ingresa Nombre Del Estudiante --> ")
    
    apellido=input("- Ingresar Apellido del Estudiante --> ")
    
    while not apellido.isalpha():
        print("---"*15)
        print("\nApellido Invalido ❌\n")
        apellido=input("- Ingresar Apellido del Estudiante --> ")

    direccion=input("- Ingresa Direccion de Residencia Del Estudiante --> ")

    email=input("- Ingresa Email Del estudiante --> ")

    telefono=input("- Ingresa Telefono Del Estudiante --> ")

    while not telefono.isnumeric():
        print("---"*15)
        print("\nTelefono Invalido ❌\n")
        telefono=input("- Ingresa Telefono Del Estudiante --> ")

    
    baseDeDatos[cedulaID]={
        "Nombre": nombre,
        "Apellido":apellido,
        "Direccion":direccion,
        "Email":email,
        "Telefono":telefono
    }

    print("---"*15)
    print("\n-> Estudiante Registrado con Exito ✅\n")
    
    for cedulaId, info in baseDeDatos.items():
        print(f"\nDocumento: {cedulaId}\nNombre: {info['Nombre']}\nApellido: {info['Apellido']}\nDireccion: {info['Direccion']}\nEmail:{info['Email']}\nTelefono: {info['Telefono']}")

    print("---"*15)

        

def buscarEstudiante():
    print("---"*15)
    print("\n** Modulo BUSCAR ESTUDIANTE **")

    if not baseDeDatos:
        print("\n-> No Hay Estudiantes , Debes Registrar Primero")
        print("---"*15)
        return
    
    
    print("\n-> Buscar Estudiante Por Documento")

    documento=input("Ingresa Documento Del Estudiante Que Deseas Buscar -> ")

    while not documento.isnumeric():
        print("Documento Invalido")
        documento=input("Ingresa Documento Del Estudiante Que Deseas Buscar -> ")

    if documento in baseDeDatos:
        documentoBuscado=baseDeDatos[documento]
        print("---"*15)
        print("Informacion Basica Del Estudiante: ")
        print("---"*15)
        print(f"Nombre: {documentoBuscado['Nombre']}\nApellido: {documentoBuscado['Apellido']}\nDireccion: {documentoBuscado['Direccion']}\nEmail: {documentoBuscado['Email']}\nTelefono: {documentoBuscado['Telefono']}")
        print("---"*15)

    else:
        print("---"*15)
        print("\n-> No existe estudiante con ese documento\n")
        print("---"*15)


def actualizarEstudiante():
    print("---"*15)
    print("\n** Modulo ACTUALIZAR ESTUDIANTE **")

    if not baseDeDatos:
        print("\n-> No Hay Estudiantes , Debes Registrar Primero")
        print("---"*15)
        return
    
    documento=input("\n-> Ingrese Documento Del Estudiante, Que Deseas Actualizar ---> ")

    while not documento.isnumeric():
        print("\nDato Invalido ❌")
        documento=input("\n-> Ingrese Documento Del Estudiante, Que Deseas Actualizar ---> ")

    if documento in baseDeDatos:

        info=baseDeDatos[documento]
        print("---"*15)
        print(f"\nEstudiante Encontrado")
        for cedulaId, info in baseDeDatos.items():
            print(f"\nDocumento: {cedulaId}\nNombre: {info['Nombre']}\nApellido: {info['Apellido']}\nDireccion: {info['Direccion']}\nEmail:{info['Email']}\nTelefono: {info['Telefono']}")
            break
        print("---"*15)
        print("\n¿Que Deseas, Actualizar?")
        print("---"*15)
        print("\n--- Opciones ---\n")
        print("1)Nombre\n2)Apellido\n3)Direccion\n4)Email\n5)Telefono")

        opcion=input("\nIngresa La Opcion --> ")
        print("---"*15)


        match opcion:
            
            case "1":
                info['Nombre']=input("Nuevo Nombre --> ")
                print("\n-> Se Actualizo Nombre Correctamente ✅")
                for cedulaId, info in baseDeDatos.items():
                    print(f"\nDocumento: {cedulaId}\nNombre: {info['Nombre']}\nApellido: {info['Apellido']}\nDireccion: {info['Direccion']}\nEmail:{info['Email']}\nTelefono: {info['Telefono']}")
                    break

            case "2":
                info['Apellido']=input("Nuevo Apellido -->")
                print("\n-> Se Actualizo Apellido Correctamente ✅")
                for cedulaId, info in baseDeDatos.items():
                    print(f"\nDocumento: {cedulaId}\nNombre: {info['Nombre']}\nApellido: {info['Apellido']}\nDireccion: {info['Direccion']}\nEmail:{info['Email']}\nTelefono: {info['Telefono']}")
                    break
            
            case "3":
                info['Direccion']=input("Nueva Direccion -->")
                print("\n-> Se Actualizo Direccion Correctamente ✅")
                for cedulaId, info in baseDeDatos.items():
                    print(f"\nDocumento: {cedulaId}\nNombre: {info['Nombre']}\nApellido: {info['Apellido']}\nDireccion: {info['Direccion']}\nEmail:{info['Email']}\nTelefono: {info['Telefono']}")
                    break
            
            case "4":
                info['Email']=input("Nuevo Email -->")
                print("\n-> Se Actualizo Email Correctamente ✅")
                for cedulaId, info in baseDeDatos.items():
                    print(f"\nDocumento: {cedulaId}\nNombre: {info['Nombre']}\nApellido: {info['Apellido']}\nDireccion: {info['Direccion']}\nEmail:{info['Email']}\nTelefono: {info['Telefono']}")
                    break
            
            case "5":
                info['Telefono']=input("Nuevo Telefono -->")
                print("\n-> Se Actualizo Telefono Correctamente ✅")
                for cedulaId, info in baseDeDatos.items():
                    print(f"\nDocumento: {cedulaId}\nNombre: {info['Nombre']}\nApellido: {info['Apellido']}\nDireccion: {info['Direccion']}\nEmail:{info['Email']}\nTelefono: {info['Telefono']}")
                    break

            case _:
                print("\nOpcion Invalida ❌")
    

    else:
        print("-> No Existe Estudiante Con ese Documento")




def eliminarEstudiante():

    if not baseDeDatos:
        print("---"*15)
        print("\n-> Debes registar Para eliminar❗")
        print("---"*15)

        return
    
    documento=input("Ingrese Documento Del estudiante a eliminar -> ")

    while not documento.isnumeric():
        print("Dato invalido")
        documento=input("Ingrese Documento Del estudiante a eliminar -> ")

    if documento in baseDeDatos:

        baseDeDatos.pop(documento)
        print("Se borro con exito ✅")
        print(baseDeDatos)

    else:
        print("No existe estudiante")

def mostrarEstudiantes():

    if not baseDeDatos:
        print("---"*15)
        print("\n-> No hay Estudiantes registrados")
        print("---"*15)

        return

    print("---"*15)
    print(f"** Estudiantes Matriculados **\n")

    for cedulaId, info in baseDeDatos.items():
        print(f"\nDocumento: {cedulaId}\nNombre: {info['Nombre']}\nApellido: {info['Apellido']}\nDireccion: {info['Direccion']}\nEmail:{info['Email']}\nTelefono: {info['Telefono']}")



constante=True

while constante:
    print("\n°°° BIENVENIDO AL COLEGIO CARRASQUILLA °°°\n")

    print("----- MENU -----\n")

    print("1) Crear Estudiante")
    print("2) Buscar Estudiante")
    print("3) Actualizar Estudiante")
    print("4) Eliminar Estudiante")
    print("5) Ver Estudiantes Matriculados")
    print("6) Salir\n")

    opcion=input("Ingresa La opcion Que Deseas --> ")

    match(opcion):

        case "1":
            crearEstudiante()

        case "2":
            buscarEstudiante()

        case "3":
            actualizarEstudiante()

        case "4":
            eliminarEstudiante()

        case "5":
            mostrarEstudiantes()

        case "6":
            break

        case _:
            print("*Opcion Invalida")