frutas = [] #declarar una lista de frutas
while True:
    add_delete = input("Agregar (A) / Eliminar (E): ")
    print(add_delete.upper())
    if add_delete == "A":
        while True:
            agregar = input("Ingresa una fruta: ")
            if agregar != "0":
                frutas.append(agregar)
                print("Para salir escribe 0")
            else:
                break
    elif add_delete == "B":
        while True:
            delete = input("Ingresar fruta: ")
        
    
print("-------FRUTAS-----------")
for i in frutas: #Recorrer e imprimir la lista
    print(i)