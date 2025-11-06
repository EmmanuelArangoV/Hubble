nota = float(input("Ingresa la nota a clasificar: "))
if nota < 3:
    print(nota, "Reprobado")
elif nota < 4.5:
    print(nota, "Aprobado")
else:
    print(nota, "Excelente")