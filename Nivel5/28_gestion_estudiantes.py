# Se declara una lista inicial de estudiantes con sus detalles
estudiantes = [
    {
        "id" : 1,
        "nombre": "Juan",
        "edad": 20,
        "cursos": ["Matemáticas", "Física"]
    },
    {
        "id" : 2,
        "nombre": "Ana",
        "edad": 22,
        "cursos": ["Química", "Biología"]
    },
    {
        "id" : 3,
        "nombre": "Luis",
        "edad": 21,
        "cursos": ["Historia", "Literatura"]
    },
    {
        "id" : 4,
        "nombre": "Marta",
        "edad": 23,
        "cursos": ["Arte", "Música"]
    },
    {
        "id" : 5,
        "nombre": "Carlos",
        "edad": 24,
        "cursos": ["Deportes", "Educación Física"]
    }
]
while True:
    print("-1 Agregar Estudiante \n-2 Eliminar Estudiante \n-3Consultar estudiante \n-0 Salir")
    res = int(input("Ingresa una opción ----> ")) # Se lee la opción del usuario
    match res:
        case 1: # Agregar estudiante
            nombre = input("Ingresa el nombre del estudiante: ")
            edad = int(input("Ingresa la edad del estudiante: "))
            cursos = input("Ingresa los cursos del estudiante separados por comas: ").split(",")
            nuevo_id = max(est["id"] for est in estudiantes) + 1
            estudiantes.append({
                "id": nuevo_id,
                "nombre": nombre,
                "edad": edad,
                "cursos": [curso.strip() for curso in cursos]
            })
        case 2: # Eliminar estudiante
            id_eliminar = int(input("Ingresa el ID del estudiante a eliminar: "))
            estudiantes = [est for est in estudiantes if est["id"] != id_eliminar]
        case 3:
            id_consultar = int(input("Ingresa el ID del estudiante a consultar: "))
            estudiante = next((est for est in estudiantes if est["id"] == id_consultar), None)
            if estudiante:
                print(f"ID: {estudiante['id']}")
                print(f"Nombre: {estudiante['nombre']}")
                print(f"Edad: {estudiante['edad']}")
                print(f"Cursos: {', '.join(estudiante['cursos'])}")
            else:
                print("Estudiante no encontrado.")
        case 0:
            break
        case _:
            print("Opción no válida.")