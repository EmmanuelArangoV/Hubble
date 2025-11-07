n = int(input("Ingresar un número: ")) #Solicitar el número al usuario

for i in range(1,11): #Usar el bucle se 1,11 para multiplicar hasta 10
    print(f"{n}X{i} --> {n*i}")