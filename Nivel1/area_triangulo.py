print("---AREA DEL TRIANGULO---")

base = float(input("Ingresa la base del triangulo -> "))
altura = float(input("Ingresa la altura del triangulo -> "))

area = (base * altura)/2
resultado_redondeado = round(area,2)

print(f"La area del triangulo es -> {resultado_redondeado}")