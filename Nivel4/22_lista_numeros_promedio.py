numeros = []
suma = 0
while True:
    n = int(input("Ingersar números enteros: "))
    if n != 0: #Si lo que ingresa el usuario es diferente de 0, se agrega a la lista, si es 0 se rompe el ciclo
        numeros.append(n)
    else:
        break

    print("Para salir ingresa 0")

for i in numeros:#Se recorre la lista de números sumandolos en la variable suma
    suma += i

print("El promedio es:", suma/len(numeros)) #se imprime el promedio (suma/(la cantidad de números que tiene la lista))