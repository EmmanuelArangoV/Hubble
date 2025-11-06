n1 = float(input("Ingresar número 1: ")) #Solicitar Número 1
n2 = float(input("Ingresar número 2: ")) #Solicitar Número 2
n3 = float(input("Ingresar número 3: ")) #Solicitar Número 3
menor=n1 # Declarar variable de menor e igualarla al número 1
mayor=n1 # Declarar variable de mayor e igualarla al número 1

if n2 < menor:# Si el n2 es < a menor, se igual a menor a n2
    menor = n2
if n3 < menor:# Si el n3 es < a menor, se igual a menor a n3
    menor = n3

if n2 > mayor: # Si el n2 es > a mayor, se igual a mayor a n2
    mayor = n2
if n3 > mayor: # Si el n3 es > a mayor, se iguala mayor a n3
    mayor = n3

print("Menor:", menor)
print("Mayor:", mayor)