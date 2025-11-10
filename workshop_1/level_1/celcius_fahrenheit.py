# Brief: Simple CLI tool to convert Celsius to Fahrenheit.
# Behavior: repeatedly prompt for a Celsius value, convert and print the Fahrenheit result.
# Validation: non-numeric input is caught and the loop continues.
# Repeat control: user is asked whether to perform another conversion; only 'Y' continues.

print("Converter Celsius to Fahrenheit degrees")

while True:
    try:
        celcius = float(input("Enter Celsius: "))
        fahrenheit = (celcius * 9 / 5) + 32
        print(f"{celcius}°C is equal to {fahrenheit}°F")
    except ValueError:
        # Invalid numeric input: inform user and prompt again
        print("Please enter a valid number.")
        continue

    # Ask the user whether to convert another temperature; continue only if 'Y'
    response = input("Would you like to convert another temperature? Press (Y) to continue: ").capitalize()
    if response != "Y":
        break