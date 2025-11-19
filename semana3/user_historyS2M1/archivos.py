import csv
import os
import tkinter as tk
from tkinter import filedialog
from servicios import validate_empty_inventory


    
def save_csv(inventario, incluir_heads=True):
    if validate_empty_inventory(inventario):
        try:
            ruta = request_ruta()
            file_exist = os.path.isfile(ruta + "/inventario.csv") # valida si el archivo existe
            with open("/home/cohorte5/Escritorio/Hubble" + "/inventario.csv", 'a', newline='', encoding='utf-8') as archivo:
                writer = csv.DictWriter(archivo, fieldnames=inventario[0].keys())
                if not file_exist: #si es True se añaden los encabezados, de lo contrario no se añaden
                    #Escribir encabezados
                    writer.writeheader()
                    
                
                #Escribir las filas
                writer.writerows(inventario)
                print("\033[32mInventario guardado en -->",ruta, "\033[0m")
        except Exception:
            print("Error al cargar información al archivo")
    else:
            print("\033[31mEl archivo no puede estar vacío\033[0m")

def load_csv():
     ruta = request_ruta("file")
     with open(ruta.name, 'r', encoding='utf-8', newline='') as archivo:
         lector = csv.reader(archivo)
         for fila in lector:
             print(fila)
         
         
    
def request_ruta(type="directory"):
    # Crear la ventana principal (aunque no la mostramos)
    root = tk.Tk()
    root.withdraw()  # No queremos mostrar la ventana principal

    if type == "file":
        # Abrir el explorador de archivos
        ruta_carpeta = filedialog.askopenfile(title="Selecciona un archivo")        
        return ruta_carpeta 
    else:
        # Abrir el explorador de archivos
        ruta_carpeta = filedialog.askdirectory(title="Selecciona una carpeta")        
        return ruta_carpeta