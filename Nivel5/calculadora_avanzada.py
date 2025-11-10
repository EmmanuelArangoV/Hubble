import math
#Calculadora avanzada

def suma(a,b):
    return a + b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a * b

def division(a,b):

    if b == 0:
        print("No se puede divir entre 0")

    return a/b

def raizCuadrada(a):

    if a < 0:
        print("No se puede calcular la raiz cuadrada de un negativo")

    return math.sqrt(a)

def potencia(a, b):
    return a ** b


def menu():

    print("\n.. Calculadora ..\n")

    print("Que opcion quieres realizar\n")

    print("" \
    "1. Sumar\n" \
    "2. Restar\n" \
    "3. Multiplicacion\n" \
    "4. Division\n" \
    "5. Potencia\n" \
    "6. Raiz Cuadrada\n" \
    "7. Salir")


binarias = {
    "1": suma,
    "2": resta,
    "3": multiplicacion,
    "4": division,
    "5": potencia
}

constante = True

while constante:
    menu()
    opcion = input("\nSelecciona una opcion -> ")

    if opcion == "7":
        print("\nSaliendo")
        break

    if opcion in binarias:
        n1 = float(input("\nIngrese el primer numero -> "))
        n2 = float(input("Ingrese el segundo numero -> "))

        operacion = binarias[opcion]
        print("Resultado -> ", operacion(n1, n2))

    elif opcion == "6":
        raiz = float(input("\nIngrese un numero -> "))

        operacion = raizCuadrada(raiz)
        print("Resultado -> ", operacion)
    
    else: 
        print("\nLa opcion no existe")

