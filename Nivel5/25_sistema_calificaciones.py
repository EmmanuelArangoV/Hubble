num_notas = int(input("Cantidad de notas a evaluar: "))
def DefinirNotas (num_notas):
    notas = []
    num_estudiantes = int(input("¿Cuantos Estudiantes vas a calificar? "))
    for i in range(num_estudiantes):
        persona = {}
        nombre = input("Inserta nombre de estudiante: ")
        persona["nombre"] = nombre
        persona["notas"] = [] 
        for i in range(num_notas):
            nota = float(input(f"Ingresa la nota #{i+1} :"))
            persona["notas"].append(nota)
        notas.append(persona)
    return notas

def CalculoNotas(num_notas):
    notas = DefinirNotas(num_notas)
    print("-----------------NOTAS----------------------")
    for i in range(num_notas):
        prom = SumaPromedioNotas(notas[i]["notas"]) 
        print("------------------//---------------//---------")
        print(f"{notas[i]["nombre"]} su nota es ---> {prom}")


def SumaPromedioNotas(arr_notas):
    suma = 0
    for i in arr_notas:
        suma += i
    return suma/len(arr_notas)

CalculoNotas(num_notas)