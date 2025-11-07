frutas = [] #declarar una lista de frutas
while True:
    agregar = input("Ingresa una fruta: ")
    if agregar != "0":
        frutas.append(agregar)
        print("Para salir escribe 0")
    else:
        break
        
print("-------FRUTAS-----------")
for i in frutas: #Recorrer e imprimir la lista
    print(i)