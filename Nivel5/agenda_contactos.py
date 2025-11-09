#Agenda de contactos
#Opciones al agendar a alguien
# las opciones serian las siguientes, agregar nuevo contacto, actualizar que seria para  el cambio de nombre, buscar un contacto, eliminar contacto, mostrar listas de contactos y por ultimo salir del proceso


#Un diccionario para guardar contactos
contactos = {}

#La primera funcion es de agregrar contactos
def agregarContacto():

    #Mostrar en que opcion se encuentra
    print("\n.... NUEVO CONTACTO ....")

    #Se preguntara de como se va a agregrar, seria el nombre, apellido y telefono
    
    #Nombre
    nombre = input("\nNombre -> ")
    #Apellido
    apellido = input("\nApellidos -> ")
    #Telefono

    telefono = input("\nTelefono -> ")

    while not telefono.isnumeric():
        print("\n❌ Incorrecto, escribe numeros")
        print("...."*15)
        telefono = input("\nTelefono -> ")

    #Un diccionario dentro de otro, para tener una llave primaria que contenga toda la info
    contactos[nombre]={
        "Apellido": apellido,
        "Telefono":telefono
    }
    print("...."*15)

    print("\n- Contacto Agregado ✅")
    print("...."*15)

    #Recorrer los contactos ya que con la funcion items se puede obtener las claves y valores por pares
    for nombre, datos in contactos.items():
        print(f"\n° Nombre = {nombre}\n° Apellido = {datos['Apellido']}\n° Telefono = {datos['Telefono']}")
        break

#Funcion Renombrar
def renombrarContacto():

    print("\n--- Renombrar Contacto ---")

    #validar si hay contactos
    if not contactos:
        print("No hay contactos aun")
        return
    
    nombre = input("Ingresa nombre de contacto -> ")
    
    #Validar si en contactos esta el nombrea ingresar para hacer el cambio
    if nombre in contactos:

        #Se genera una variable para guardar el valor obtenido del diccionario contactos por su clave nombre
        datos = contactos[nombre]
        print("\nQue deseas renombrar? \n")

        print("1) Nombre\n" \
            "2) Apellido")
        
        seleccion = input("\nSeleciona la opcion -> ")
        print("...."*15)
        
        #Las opciones para el cambio
        match seleccion:
            case "1":
                nuevo_nombre = input("\nNuevo nombre -> ")

                #Hacer el cambio del nuevo nombre con el que ya existe y luego eliminar el anterior
                contactos[nuevo_nombre] = contactos[nombre]
                #eliminar
                del contactos[nombre]

                print("Cambio con exito ✅")
                #Recorrer los contactos ya que con la funcion items se puede obtener las claves y valores por pares
                for nombre, datos in contactos.items():
                    print(f"\n° Nombre = {nombre}\n° Apellido = {datos['Apellido']}\n° Telefono = {datos['Telefono']}")
        
            case "2":
                #Se hace el cambio del apellido 
                datos['Apellido'] = input("Nuevo apellido -> ")
                print("Cambio con exito")
                
                #Recorrer los contactos ya que con la funcion items se puede obtener las claves y valores por pares
                for nombre, datos in contactos.items():
                    print(f"\n° Nombre = {nombre}\n° Apellido = {datos['Apellido']}\n° Telefono = {datos['Telefono']}")
            case _:
                print("Opcion no valida")
    else: 
        print("\nNo existe ese contacto")

def buscarContacto():
    print("... BUSCAR CONTACTO ...")

    if not contactos:
        print("\nNo hay contactos aun")

    nombre = input("\nIngrese el nombre del contacto -> ")

    if nombre in contactos:
        buscar = contactos[nombre]
        
        print(f"\nNombre: {nombre}\nApellido: {buscar['Apellido']}\nTelefono: {buscar['Telefono']}")
    else:
        print("\nNo existe ese contacto")

def verContactos():

    print("\n... LISTA DE CONTACTOS ...")

    if not contactos:
        print("\nNo hay ningun contacto")

    #Recorrer los contactos ya que con la funcion items se puede obtener las claves y valores por pares
    for nombre, datos in contactos.items():
        print(f"\n° Nombre = {nombre}\n° Apellido = {datos['Apellido']}\n° Telefono = {datos['Telefono']}")

def eliminarContacto():

    print("\n... ELIMINAR CONTACTO ...")

    if not contactos:
        print("\nNo hay contactos aun")
        return
    
    nombre = input("Escribe el nombre del contacto a eliminar -> ")

    if nombre in contactos:
        contactos.pop(nombre)
        print("\nContacto eliminado")
    else:
        print("Contacto no existe")















#Siempre sera verdadero de lo contrario no funcionaria 
constante = True

#bucle para que vuelva a las opciones
while constante:
#mostrar titulo de opciones y de que es el programa
    print("...."*15)
    print("... AGENDA DE CONTACTOS ...")
    print("\n--- OPCIONES ---")

    #Mostrar las opciones que se pueden realizar
    print(
    "1 - Agregar Nuevo Contacto\n" \
    "2 - Renombrar Contacto\n" \
    "3 - Buscar Contacto\n" \
    "4 - Ver Contactos\n"\
    "5 - Eliminar Contacto\n" \
    "6 - Salir"
    )

    opciones = input("\n- Ingrese la opcion -> ")

    #Realizar una estructura de las opciones que hay mas eficiente para llamar la funcion de cada una
    match opciones:
        case "1":
            agregarContacto()
        case "2":
            renombrarContacto()
        case "3":
            buscarContacto()
        case "4":
            verContactos()
        case "5":
            eliminarContacto()
        case "6":
            break
        case _:
            print("\nNo existe esa opcion")
