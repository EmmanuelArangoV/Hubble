#Solicitar número 1 y número 2 al usuario
n1 = float(input("Ingresa un número: "))
n2 = float(input("Ingresa otro número: "))

simbolo = input("¿Qué operación quieres realizar? (+,-,*,/)")
# Operaciones básicas
if simbolo == "+":
    #Suma
    print("Suma: ", n1+n2)
elif simbolo == "-":
    #Resta
    print("Resta: ", n1-n2)
elif simbolo == "*":
    #Multiplicación
    print("Multuplicación: ", n1*n2)
elif simbolo == "/":
    #División
    print("División: ", n1/n2)
else:
    print("Operación no válida")
