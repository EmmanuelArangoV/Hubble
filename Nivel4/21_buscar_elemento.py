frutas = ["pera","manzana", "banano", "sandia"] #declarar una lista de frutas
buscar = input("Ingrese la fruta a buscar: ").lower() #Convertir a lower para que coincida lo que ingresa el usuuario con la lista
flag =False #Definir una bandera para igaularla True si existe la fruta
for i in frutas:
    if i == buscar:#si existe la fruta la bandera se iguala a True y si existe se rompe el ciclo
        flag = True
        break

if flag: #Si la bandera es verdadera imprime que existe, si no existe, imprime que no existe
    print(f"La fruta {buscar.upper()} si existe en la lista")
else:
    print(f"La fruta {buscar.upper()} no existe en la lista")