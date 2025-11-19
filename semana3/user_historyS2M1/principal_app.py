import servicios
import archivos

product_list = []


while True:
    try:
        res = int(input("¿Qué deseas hacer? \n1-Agregar producto \n2-Mostrar Inventario \n3-Calcular estadísticas\n7-Guardar CSV\n8-Cargar CSV \n0-Salir \n---> "))
        match res:
            case 1:
                res = "yes"
                while True:
                    if res == "yes":
                        product_list.append(servicios.create_product())
                    elif res == "no":
                        print("Aborting")
                        break
                    else:
                        print("Digita Yes/No")
                        
                    res = input("¿Deseas continuar agregando productos? yes/no: ").lower()
            case 2:
                servicios.show_inventory(product_list)
            case 3:
                servicios.calculate_stats(product_list)
                print(product_list)
            case 7:
                archivos.save_csv(product_list)
                product_list.clear()
            case 8:
                archivos.load_csv()
            case 0:
                break
            case _:
                print('\033[31mOpción no válida\033[0m')
    except ValueError:
        print("\033[31mIngresa un valor válido\033[0m")
        
