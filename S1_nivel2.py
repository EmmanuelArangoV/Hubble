'''print()
print()
print("EJERCICIO: MAYOR DE EDAD")
while True:
    edad = int(input("Digita tu edad: "))
    if edad > 0 and edad <90:
        if edad >=18:
            print("Enhorabuena, eres mayor de edad")
        else:
            print("Eres menor de edad")
        break
    else:
        print("La edad es incorrecta, intentalo nuevamente: ")'''

'''print()
print()
print("EJERCICIO: NUMERO POSITIVO, NEGATIVO O CERO")
numero = float(input("Digite un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es igual a cero")
else:
    print("El numero es negativo")'''

'''print()
print()
print("EJERCICIO: PAR O IMPAR")
numero = int(input("Digite un numero: "))
if numero %2 ==0:
    print("El numero es par")
else:
    print("El numero es impar")'''

print()
print()
print("EJERCICIO: CALCULADORA BASICA CON +,-,*,/")
print("1: Suma")
print("2: Resta")
print("3: Multiplicacion")
print("4: Division")

selec = int(input("Ingresa la opcion para la operacion que de deseas realizar: "))

num1 = float(input("Digite un numero: "))
num2 = float(input("Digite el segundo numero: "))

if selec == 1:
    resultado= num1 + num2
elif selec == 2:
    resultado = num1 - num2
elif selec == 3:
    resultado = num1 * num2
elif selec == 4:
    resultado = num1 / num2
else:
    print("Esta opcion es incorrecta")
print(f"Tu resultado es: {resultado}" )




  