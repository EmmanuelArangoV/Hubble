print()
print()
print("EJERCICIO: HOLA USUARIO")
#Se pide nombre y edad al usuario por consola#
nombre = input("Por favor digita tu nombre: ")
edad = int(input("Ahora digita tu edad: "))
#Se imprime el un saludo con los datos ingresados del usuario#
print(f"Hola {nombre} tienes {edad} años de de edad")
print()
print()

print("EJERCICIO: SUMA DE DOS NUMEROS")
#Se pide al usuario el primer numero#
num1 = int(input("Digita el primer numero: "))
#Se pide al usuario el segundo numero#
num2 = int(input("Digita el segundo numero: "))
#Se crea una variable que contenga la opeacion que se pide: suma#
suma = num1 + num2
#Resultado de la suma de los valores ingresados del usuario#
print(f"La suma es: {suma}")
print()
print()

print("EJERCICIO: AREA DE TRIANGULO")
#Se le pide al usuario primer dato del triangulo: base#
base = float(input("Ingrese la base del triangulo en cms: "))
#Se le pide al usuario segundo dato del triangulo: altura#
altura = float(input("Ingrese la altura del triangulo cms: "))
#Se crea variable para calcular area del triangulo mediante la formula matematica A=b*h/2#
area = (base*altura)/2
#Resultado de laformula con los datos que el usuario ingresó#
print(f"El area del triangulo es: {area} cm\u00b2")
print()
print()

print("EJERCICIO: CONVERSOR DE GRADOS CELSIUS A FAHRENHEIT")
#Se le pide al usuario que ingrese su temperatura en celsius#
celsius = float(input("Digita tu temperatura en celsius para convertirlos a Fahrenheit: "))
#Se crea variable con la formula de la conversion de celsius a fahrenheit: F=(C*9/5)+32#
Fahrenheit = (celsius*9/5)+32
#Se imprime la reaultado de la coversion a fahrenheit#
print(f"La conversion de celcius a Fahrenheit es: {Fahrenheit}°F")
print()
print()

print("EJERCICIO: TIPO DE DATOS")
#Se crea variables para cada tipo de datos con su respectivo contenido#
nombre = input("Digita tu primer nombre: ")
edad = int(input("Digita tu edad: "))
estatura = float(input("Digita tu altura: "))
booleano = True
lista = [1,2,3,4]
tuplita = (1,2,3,4)
diccionario = {nombre:"Luis", edad:22, estatura:1.70, booleano:True}
#Se imprime usando la funcion type para mostrar el tipo de dato de cada variable#
print(f"Tu nombre es: {type(nombre)}")
print(f"Tu edad es: {type(edad)}")
print(f"Tu estatura es: {type(estatura)}")
print(type(booleano))
print(type(lista))
print(type(tuplita))
print(type(diccionario))
print()
print()

print("EJERCICIO: EDAD FUTURA")
#Se pide nombre y edad al usuario por consola#
nombre = input("Por favor digita tu nombre: ")
edad = int(input("Ahora digita tu edad: "))
#Se crea una variable donde le incrementara el valor que le di en este caso 10#
contador = +10
#Se imprime el un saludo con los datos ingresados del usuario con su edad dentro de 10 años realizando una operacion aritmetica entre 2 variables#
print(f"Hola {nombre} tienes {edad} años de de edad y en 10 años tendras: {edad+contador} años de edad, vamos pa viejo")