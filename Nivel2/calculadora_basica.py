num1 = int(input("Ingresa un numero -> "))
num2 = int(input("Ingresa otro numero -> "))

operacion = input("Cual de las siguientes operaciones quieres realizar -> \n + \n - \n * \n / \n -> ")

if operacion == "+":
    sumaTotal=num1 + num2
    print(f"La suma de {num1} + {num2} es = {sumaTotal}")
elif operacion == "-":
    restaTotal=num1 - num2
    print(f"La resta de {num1} - {num2} es = {restaTotal}")
elif operacion == "*":
    multiplicacionTotal=num1 * num2
    print(f"La suma de {num1} * {num2} es = {multiplicacionTotal}")
elif operacion == "+":
    divisionTotal=num1 / num2
    print(f"La suma de {num1} / {num2} es = {divisionTotal}")
else:
    print("Operacion no valida")