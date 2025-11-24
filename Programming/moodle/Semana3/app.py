import csv
import os
import tkinter as tk
from tkinter import filedialog
from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, estadisticas
from archivos import guardar_csv, cargar_csv
inventario = [
    {"nombre": "Manzana", "precio": 1500, "cantidad": 10},
    {"nombre": "Banana", "precio": 1100, "cantidad": 20},
    {"nombre": "Fresa", "precio": 3000, "cantidad": 15},
    {"nombre": "Pera", "precio": 2800, "cantidad": 12},
    {"nombre": "Uva", "precio": 4000, "cantidad": 8},
    {"nombre": "Tomate", "precio": 1500, "cantidad": 30},
    {"nombre": "Zanahoria", "precio": 1000, "cantidad": 25},
    {"nombre": "Brocoli", "precio": 2300, "cantidad": 10},
    {"nombre": "Espinaca", "precio": 1800, "cantidad": 18},
    {"nombre": "Pepino", "precio": 1200, "cantidad": 22},
    {"nombre": "Arroz", "precio": 3000, "cantidad": 50},
    {"nombre": "Frijoles", "precio": 1000, "cantidad": 40},
    {"nombre": "Lentejas", "precio": 2000, "cantidad": 30},
    {"nombre": "Maiz", "precio": 1100, "cantidad": 35},
    {"nombre": "Arberjas", "precio": 3500, "cantidad": 12}
]

print("Tiendita Li: Bienvenido que deseas realizar:\n")

while True:
    print("\n¿Que accion desea realizar?")
    print("==>1. Agregar producto")
    print("==>2. Mostrar inventario")
    print("==>3. Buscar producto")
    print("==>4. Actualizar producto")
    print("==>5. Eliminar producto")
    print("==>6. Calcular estadistica")
    print("==>7. Guardar CSV")
    print("==>8. Cargar CSV")
    print("==>0. Salir \n")


    opcion = input("\nDigita el numero de tu opcion: ")
    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        buscar_producto(inventario) 
    elif opcion == "4":
        actualizar_producto(inventario)
    elif opcion == "5":
        eliminar_producto(inventario)
    elif opcion == "6":
        estadisticas(inventario)
    elif opcion == "7":
        guardar_csv(inventario)
    elif opcion == "8":
        cargar_csv(inventario)
    elif opcion == "0":
        confirmacion = input("\n¿Esta seguro de salir del sistema?: si/no: ")
        if confirmacion == "si":
            print("Saliendo del sistema...")
            break
        else:
            print("Volviendo al sistema")           
    else:
        print("==>Digita una opcion que este en el rango de 0-8<==")