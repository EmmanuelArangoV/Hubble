import csv
import os

class CRUD:
    def crear_archivo(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["id", "nombre", "edad"])


    def incrementar_id(self, archivo):
        with open(archivo, 'r') as file:
            filas = list(csv.reader(file))

        if len(filas) == 1:
            return 1
            
        ultimo_id = int(filas[-1][0])
        return ultimo_id + 1
    
    def crear(self, archivo, nombre, edad):
        id_nuevo = self.incrementar_id(archivo)
        with open(archivo , 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id_nuevo, nombre, edad])
            return id_nuevo
    

    def listar(self, archivo):
        with open(archivo, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            return list(reader)
    
    def eliminar_por_id(self, archivo, id_eliminar):
        data = self.listar(archivo)
        for persona in data:
            if persona[0] == id_eliminar:
                data.remove(persona)
                self.sobreescribir(archivo, data)
                break
            
            print("El ID no se encontró")

    def sobreescribir(self, archivo, data):
        with open(archivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "nombre", "edad"])
            for fila in data:
                writer.writerow(fila)

