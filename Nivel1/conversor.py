print("---CELSIUS A FAHRENHEIT")

celsius = float(input("Ingresa los grados celsius para convertir -> "))

fahrenheit = (celsius * 9/5) + 32
resultado_redondeado = round(fahrenheit, 2)

print(f"Los {celsius}°C a Fahrenheit es -> {fahrenheit}°F")
