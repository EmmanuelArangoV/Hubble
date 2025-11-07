print("-- Tienda Ropa --\n")

carritoCompras = []

opciones = input("1.Elegir Prenda\n" \
"2.Eliminar prenda\n" \
"3.Pagar \n-> ")


prendas = {"camisa":10000,"\npantalon":40000,"\nvestido":25000,"\nzapatos":100000}


if opciones == "1":
    print(prendas)

    prenda = input("Selecciona la prenda que quieres comprar -> ")
    carritoCompras.append(prendas[prenda])
    print(prenda, carritoCompras)

    



