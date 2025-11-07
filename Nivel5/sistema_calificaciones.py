

while True:
    respuesta = input("\n¿Quieres ingresar un nombre? -> ")
    if respuesta == "no":
        break

    estudiantes = {"valeria": [4.5, 4.4, 4.3], "sebas": [3.0, 2.5, 5.0], "luis":[5.0, 4.5, 5.0]}

    nombre = input("Ingrese el nombre -> ")

    estudianteactual = estudiantes[nombre]

    suma = 0
    for notas in estudianteactual:
        suma = suma + notas

    promedio = suma / len(estudianteactual)
    promedio_redondeado = round(promedio,2)

    print(f"\n--{nombre} \nEstas son tus notas\n")

    for notas in estudianteactual:
        print(notas)

    if promedio < 3.0:
        print(f"Tu promedio = {promedio_redondeado} y Reprobaste")
    elif promedio < 4.7:
        print(f"Tu promedio es de = {promedio_redondeado} y aprobaste")
    else:
        print(f"\nTu promedio es de = {promedio_redondeado}, excelente nota!")

