#Ejercicio 20
frutas = ["pera","manzana","sandia","banano"]

print(frutas)

agregar = input("\n¿Cual fruta deseas agregar? -> ")
frutas.append(agregar)

print(f"\nAGREGADO\n{frutas}")

elimina_fruta = input("\n¿Cual fruta deseas eliminar? -> ")

frutas.remove(elimina_fruta)
print(f"\n{frutas}")

#Ejercicio 21
buscar =  input("\nIngresa la fruta que quieres buscar -> ")

if buscar in frutas:
    print("Si esta en la lista")
else:
    print("no se encuentra en la lista")