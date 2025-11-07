numeros = []
while True:
    numero = int(input("Ingresar número (Solo se guardarán números pares): "))
    if numero != 0:
        if numero%2 == 0:
            numeros.append(numero)
    else:
        break
    print("Para salir escribe 0")

for i in numeros:
    print(i)