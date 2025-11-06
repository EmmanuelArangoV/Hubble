#Solicitar nota
nota = float(input("Ingresa la nota a clasificar: "))

if nota < 3:# si nota es menor a 3 es reprobado
    print(nota, "Reprobado")
elif nota < 4.5:# si está entre el 3 y 4.4 es Aprobado
    print(nota, "Aprobado")
else:
    print(nota, "Excelente") #Si no cumple las anteriores, es excelente