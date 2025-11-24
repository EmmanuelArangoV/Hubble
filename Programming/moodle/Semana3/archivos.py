import csv
import os
import tkinter as tk
from tkinter import filedialog

def guardar_csv(inventario):
    """
    Función para guardar el inventario en un archivo CSV
    """
    if not inventario:
        print("El inventario está vacío. No se puede guardar el archivo.")
        return False
    try:
        root = tk.Tk()
        root.withdraw()
        
        ruta = filedialog.asksaveasfilename(
            title="Guardar inventario como CSV",
            defaultextension=".csv",
            filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")],
            initialdir=os.getcwd()
        )
        if not ruta:
            print("Operación de guardado cancelada.")
            root.destroy()
            return False
        with open(ruta, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["nombre", "precio", "cantidad"])
            for producto in inventario:
                writer.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])
        print(f"✅ Inventario guardado exitosamente en: {ruta}")
        print(f"📊 Total de productos guardados: {len(inventario)}")
        root.destroy()
        return True 
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
        return False

def cargar_csv(inventario):
    """
    Función para cargar inventario desde archivo CSV
    """
    filas_invalidas = 0
    productos_cargados = 0
    try:
        root = tk.Tk()
        root.withdraw()        
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo CSV para cargar",
            filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")],
            initialdir=os.getcwd()
        )      
        if not ruta:
            print("❌ No se seleccionó ningún archivo.")
            root.destroy()
            return False 
        with open(ruta, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            encabezado = next(reader)    
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("❌ Error: Formato de archivo inválido.")
                root.destroy()
                return False
            print("\n📥 OPCIONES DE CARGA:")
            print("1. Sobrescribir inventario actual")
            print("2. Fusionar con inventario actual")
            while True:
                opcion = input("Selecciona (1/2): ").strip()
                if opcion in ["1", "2"]:
                    break
                print("❌ Opción inválida. Por favor ingresa 1 o 2.")
            inventario_temporal = []
            if opcion == "1":
                print("🔄 Inventario actual será reemplazado.")
            else:
                inventario_temporal = inventario.copy()
                print("🔄 Se fusionará con inventario actual.")
            for num_fila, fila in enumerate(reader, start=2):
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                nombre, precio_str, cantidad_str = fila
                nombre = nombre.strip().capitalize()
                try:
                    precio = float(precio_str)
                    cantidad = int(cantidad_str)
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue
                    producto_existente = next((p for p in inventario_temporal if p["nombre"] == nombre), None)
                    if producto_existente:
                        producto_existente["cantidad"] += cantidad
                        producto_existente["precio"] = precio
                    else:
                        inventario_temporal.append({
                            "nombre": nombre, 
                            "precio": precio, 
                            "cantidad": cantidad
                        })
                    productos_cargados += 1   
                except ValueError:
                    filas_invalidas += 1
                    continue
            inventario.clear()
            inventario.extend(inventario_temporal)
            print(f"\n✅ CARGA COMPLETADA:")
            print(f"   📦 Productos cargados: {productos_cargados}")
            print(f"   ⚠️  Filas omitidas: {filas_invalidas}")
            print(f"   📊 Total en inventario: {len(inventario)} productos")
        root.destroy()
        return True
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False