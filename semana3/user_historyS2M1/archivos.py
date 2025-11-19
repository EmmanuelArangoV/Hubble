import csv
import tkinter as tk
from tkinter import filedialog


    
def save_csv(inventario):
    fieldsnames = inventario[0].keys()
    ruta = request_ruta()
    try:
        with open(ruta + "/inventario.csv", 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=fieldsnames)
            
            #Escribir encabezados
            writer.writeheader()
            
            #Escribir las filas
            writer.writerows(inventario)
    except ValueError:
        print("Error al cargar información al archivo")
    
    
def request_ruta():
    # Crear la ventana principal (aunque no la mostramos)
    root = tk.Tk()
    root.withdraw()  # No queremos mostrar la ventana principal

    # Abrir el explorador de archivos
    ruta_carpeta = filedialog.askdirectory(title="Selecciona una carpeta")        
    return ruta_carpeta