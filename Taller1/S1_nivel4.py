'''print()
print()
print("EJERCICIO: LISTA DE FRUTAS")
print("manzana, pera, naranja, platano, cereza")

print()
print()
print("EJERCICIO: AGREGAR Y ELIMINAR FRUTAS")
frutas = ["manzana", "pera", "naranja", "platano", "cereza"]
print(f"Lista inicial de frutas: {frutas}")
fruta_agregar = input("Ingrese una fruta diferente que no este en la lista para agregar a la lista: ")
frutas.append(fruta_agregar)
print(f"Lista actualizada de frutas: {frutas}")
fruta_eliminar = input("Ingrese una fruta para eliminar de la lista: ")
if fruta_eliminar in frutas:
    frutas.remove(fruta_eliminar)
    print(f"Lista actualizada de frutas: {frutas}")

print()
print()
print("EJERCICIO: BUSCAR UN ELEMENTO EN LISTA")
frutas = ["manzana", "pera", "naranja", "platano", "cereza"]
print(f"Lista de frutas: {frutas}")
buscar = input("Ingrese una fruta que desee buscar: ")
buscar_minuscula = buscar.lower()
if buscar_minuscula in frutas:
    print("La fruta se encuentra en la lista.")
else:
    print("La fruta no se encuentra en la lista.")

print()
print()
print("EJERCICIO: LISTA DE NUMEROS Y NUMEROS")
numeros = [1, 2, 3, 4, 5]
print(f"Lista de numeros: {numeros}")
suma = sum(numeros)
promdio = suma / len(numeros)
print(f"El promedio de los numeros es: {promdio}")

print()
print()
print("EJERCICIO: NUMEROS PARES")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numeros:
    if num %2==0:
        pares.append(num)
print(f"Los numeros pares en la lista son: {pares}")'''

print()
print()
print("EJERCICIO: ELIMINAR DUPLICADOS")
numeros = [1, 2, 2, 3, 4, 4, 5]
print(f"Lista inicial de numeros: {numeros}")
numeros_sin_duplicados = list(set(numeros))
print(f"Lista de numeros sin duplicados: {numeros_sin_duplicados}")
