#definir funciones para cada operacion
def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division por cero no es permitida."
    
while True: #bucle con validacion de opciones
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("0. Salir")
    
    opcion = input("Ingrese su opción ----> ")
    if opcion == '0':#romper el ciclo, si es 0 antes de solicitar los numeros y entrar al match
        break
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    match opcion: #casos para cada operacion
        case '1':
            print(f"--------------Resultado: {suma(num1, num2)}--------------")
        case '2':
            print(f"--------------Resultado: {resta(num1, num2)}--------------")
        case '3':
            print(f"--------------Resultado: {multiplicacion(num1, num2)}--------------")
        case '4':
            print(f"--------------Resultado: {division(num1, num2)}--------------")
        case _:
            print("Opción no válida. Por favor intente de nuevo.")