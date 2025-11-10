'''print()
print()
print("EJERCICIO: CONTAR DEL 1 AL 10")
#Usando un bucle for para contar del 1 al 10#
for i in range(1,10):
    print(i)

print()
print()
print("EJERCICIO: SUMATORIA DEL 1 AL N")
n = int(input("Ingresa un numero: "))
#Se inicializa esta variable en 0#
suma = 0
#Usando un bucle for para sumar del 1 al n#
for i in range(1,n+1):
    suma = suma+i
    print(suma)

print()
print()
print("EJERCICIO: TABLA DE MULTIPLICAR")
numero = int(input("Ingrese el numero que desea para ver su tabla de multiplicar: "))
#Se inicializa esta variable en 0#
multiplicador = 0
#Usando un bucle for para mostrar la tabla de multiplicar del numero ingresado#
for i in range(1, 10+1):
    multiplicador = numero*i
    print(f"{numero} x {i} ==> {multiplicador}")

print()
print()
print("EJERCICIO: CONTADOR REGRESIVO WHILE")
n = int(input("Ingresa un numero: "))
#Se inicializa esta variable en 5 segun la actividad#
contador = 5
#Usando un bucle while para hacer el conteo regresivo#
while contador > 0:
#A la variable se le ira restando uno#
    contador -=1
    print(contador)

print()
print()
#Se importa una libreria#
import random
print("EJERCICIO: ADIVINA EL NUMERO")
print("El numero esta entre el 1 y el 25")
secreto = random.randint(1,26)
#Usando un bucle while para adivinar el numero#
while True:
    n = int(input("Ingresa un numero: "))
    if secreto == n:
        print("Adivinaste el numero")
        break
    else:
        print("Intentalo nuevamente")'''

print()
print()
print("EJERCICIO: SUMAR HASTA QUE EL USUARIO ESCRIBA 0")
suma = 0
#Usando un bucle while para sumar los numeros que ingrese el usuario hasta que ingrese un 0#
while True:
    n = int(input("Ingresa un numero (ingresa 0 para terminar): "))
    if n == 0:
        print(f"La suma total es: {suma}")
        break
    else:
        suma += n
        print(f"Suma actual: {suma}")