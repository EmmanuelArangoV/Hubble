suma = 0
while True:
    res = int(input("Ingrese un número para sumar: "))
    if res >= 0: #Si el usuario ingresa un valor positivo se sumará el valor en la variable suma
        suma += res
        print("Si desea salir ingresa 0")
        if res == 0: # Si el usuario digita 0 se rompe el ciclo
            break
    else:
        print("Ingrese un número mayor a 0")

print("La suma es:", suma)