while True:
    n = int(input("Ingresar un número desde donde se iniciará la cuenta regresiva: ")) #Solicitar el número al usuario
    if n > 0: # si se cumple la condición se rompe el siclo
        break

while n > 0: #El ciclo será True y se ejecutará mientras n sea mayor a 0
    print(n) 
    n -=1 #resto 1 a n