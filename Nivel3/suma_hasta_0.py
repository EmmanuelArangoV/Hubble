resultado = 0

while True:
    num_ingresado = int(input("Ingresa un numero -> "))

    if num_ingresado == 0:
        print(f"resultado final:{resultado}")
        break
    resultado += num_ingresado