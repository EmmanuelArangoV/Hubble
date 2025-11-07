n = int(input("Ingresar un número: ")) #Solicitar el número al usuario
sumatoria = 0
for i in range(1,n+1): #Usar el bucle se 1,n+1 para tomar el número que ingresó el usuario
    sumatoria += i #sumar el iterador a la variable sumatoria
print(f"La sumatoria de los numeros del los números de 1 hasta {n} es: {sumatoria}")