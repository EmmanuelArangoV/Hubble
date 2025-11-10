usuarios={}


def registrarUser():
    print("---"*10)
    print("\nBienvenido Al Banco Tio Donal")
    user=input("\nIngrese Nombre del Usuario --> ")

    if user in usuarios:
        print("\nUsuario Existente")
        return
    
    constante=True

    while constante:
        saldoIncial=input("\nIngrese Saldo Inicial --> ")

        if saldoIncial.isdigit() and int(saldoIncial)>0:
            saldoIncial=int(saldoIncial)
            break
        else:
            print("\nIngresa un saldo inicial mayor a 0")

    while constante:
        password=input("\nCrea una contraseña --> ")
        password=password.replace(" ","")

        if password != " ":
            break
        else:
            print("\nLa contraseña no puede estar Vacia")
    
    usuarios[user]={
        "saldo":saldoIncial,
        "pass":password
    }
    print("---"*15)
    print(f"\nUsuario {user} Registrado Exitosamente")
    print("---"*15)


def loguearseEnElCajero():
    print("---"*15)
    print("\nBienvenido Al cajero Tio Donal")
    print("---"*10)
    user=input("\nIngrese Usuario --> ")

    if user not in usuarios:
        print("\nEste Usuario No Existe")
        print("---"*15)
        return False
    password=input("Ingrese Password --> ")
    
    if usuarios[user]['pass']==password:
        print(f"\nBienvenido de Nuevo, {user}")
        return user
    else:
        print("\nContraseña Incorrecta")
        return False
    

def menu():
    print("---"*15)
    print("\nOpciones Cajero")
    print("\n1)Consultar Saldo\n2)Depositar Dinero\n3)Retira Dinero\n4)Cerrar sesion")


def consultarSaldo(user):
    print("---"*15)
    print(f"\nTu saldo Actual es de {usuarios[user]['saldo']}")

def depositarDinero(user):
  
    
    

        dinero=input("\nIngrese Dinero a Depositar --> ")

        if dinero.isdigit() and int(dinero)>0:
            dinero=int(dinero)
            usuarios[user]['saldo'] +=dinero
            print(f"\nDinero Ingresado -> {dinero} , Nuevo Saldo -> {usuarios[user]['saldo']}")
            
        else:
            print("Ingrese un valor mayor a 0")


def retirarDinero(user):
    
    

   
        dinero=input("\nIngrese Dinero a Retirar --> ")

        if dinero.isdigit() and int(dinero)>0:
            dinero=int(dinero)
            if dinero > usuarios[user]['saldo']:
                print("\nSaldo Insuficiente")
            else:
                usuarios[user]['saldo'] -=dinero
                print(f"\nRetiraste -> {dinero} y tu nuevo saldo es de -> {usuarios[user]['saldo']}")
        else:
            print("\nIngrese un valor mayor a 0")


constate=True

while constate:
    print("\nBienvenido al cajero del tio Donal")
    print("---"*15)
    print("\n1)Registar Usario\n2)Iniciar Sesion\n3)Salir del cajero")

    opcion=input("\nIngrese Opcion --> ")

    match opcion:
        case "1":
            registrarUser()
        case "2":
            estadoUser=loguearseEnElCajero()

            if estadoUser:

                constate=True

                while constate:

                    menu()

                    opcionesCajero=input("\nIngrese Una opcion -> ")

                    match opcionesCajero:

                        case "1":
                            consultarSaldo(estadoUser)

                        case "2":
                            depositarDinero(estadoUser)

                        case "3":
                            retirarDinero(estadoUser)
                        case "4":
                            print("---"*15)
                            print(f"Sesion cerrada {estadoUser}")
                            print("---"*15)
                            break
                        case _:
                            print("Opcion Invalida")

        case "3":
            print("\nGracias por usar el cajero del tio Donal!\n")
            break
         
        case _:
            print("\nOpcion Invalida")
            print("---"*15)