'''print()
print()
print("EJERCICIO: CONTAR DEL 1 AL 10")
for i in range(1,10):
    print(i)'''

'''print()
print()
print("EJERCICIO: SUMATORIA DEL 1 AL N")

n = int(input("Ingresa un numero: "))
suma = 0
for i in range(1,n+1):
    suma = suma+i
    print(suma)'''

'''print()
print()
print("EJERCICIO: TABLA DE MULTIPLICAR")
numero = int(input("Ingrese el numero que desea para ver su tabla de multiplicar: "))
multiplicador = 0
for i in range(1, 10+1):
    multiplicador = numero*i
    print(f"{numero} x {i} ==> {multiplicador}")'''

'''print()
print()
print("EJERCICIO: CONTADOR REGRESIVO WHILE")
n = int(input("Ingresa un numero: "))
contador = 5
while contador > 0:
    contador -=1
    print(contador)'''

'''print()
print()
import random
print("EJERCICIO: ADIVINA EL NUMERO")
print("El numero esta entre el 1 y el 25")
secreto = random.randint(1,26)
while True:
    n = int(input("Ingresa un numero: "))
    if secreto == n:
        print("Adivinaste el numero")
        break
    else:
        print("Intentalo nuevamente")'''
        