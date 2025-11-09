total_compra = 0
carrito = []
articulos = {
    "camisa":{
        "tipo": "camisa",
        "talla": "xl",
        "precio": 1200
    },
    "jean": {
        "tipo": "jean",
        "talla": 32,
        "precio": 2000
    },
    "zapatos": {
        "tipo": "zapatos",
        "talla": 40,
        "precio": 5000
    }
}
while True:
    print("-1 Agregar \n-2 Eliminar \n-0 Salir")

    r = int(input("Ingresa una opción ----> "))
    match r:
        case 1:
            prod = input("Que producto desea agregar?\ncamisa\nJean\nzapatos\n ----> ").lower()
            carrito.append(articulos[prod])
        case 2:
            prod = input("Que producto desea eliminar?\ncamisa\nJean\nzapatos\n ----> ").lower()    
            carrito.remove(articulos[prod])
        case 0:
            break
        case _:
            print("opción no valida")
print("----------------Tú Carrito de compras------------------")
print("Articulo   ||   Precio")
for art in carrito:
    total_compra += art["precio"]
    print(art["tipo"],               "||",   art["precio"])
print("Total --->  ",total_compra) 