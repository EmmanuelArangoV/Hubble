import csv
import os
import tkinter as tk
from tkinter import filedialog

fieldnames = ['name','price','amount']
    
def save_csv(inventario, incluir_heads=True):
    if len(inventario):
        try:
            ruta = request_ruta()
            file_exist = os.path.isfile(ruta + "/inventario.csv") # valida si el archivo existe
            with open(ruta + "/inventario.csv", 'a', newline='', encoding='utf-8') as archivo:
                writer = csv.DictWriter(archivo, fieldnames=fieldnames)
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
         lector = csv.DictReader(archivo)
         return list(lector)
     
def add_inventory_csv():
    ruta = os.getcwd()
    data = load_csv()
    with open(ruta + "/inventario.csv", 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        writer.writerows(data)
        return f"\033[32mProducto agregado en --> {ruta} \033[0m"

def overwrite_csv(ruta):
    lista_nueva = load_csv()
    with open(ruta + "/inventario.csv", 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        #Escribir encabezados
        writer.writeheader()
        writer.writerows(lista_nueva)
        return "Archivo sobreescrito"
    
def cargar_csv():
    ruta = request_ruta()
    print(ruta + "/inventario.csv")
    if os.path.exists(ruta + "/inventario.csv"):
        opcion = input("Desea sobreescribir el archivo? S/n ").lower()
        if opcion == 's':
            print(overwrite_csv(ruta))
        elif opcion == 'n':
            print(add_inventory_csv())
            print("agregar")
        else:" opcion invalida"

                 
    
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