print("Converter Celsius to Fahrenheit degrees")

while True:
    try:
        celcius = float(input("Enter Celsius: "))
        fahrenheit = (celcius * 9 / 5) + 32
        print(f"{celcius}°C is equal to {fahrenheit}°F")
    except ValueError:
        print("Please enter a valid number.")
        continue

    response = input("Would you like to convert another temperature? Press (Y) to continue: ").capitalize()
    if response != "Y":
        break