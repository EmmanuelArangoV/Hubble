print("Welcome to regressive counter.")

while True:
    try:
        number = int(input("Please enter the number: "))
        # Comportamiento decreciente: el número es mayor o igual a 0, cuenta regresiva hasta 0.
        if number >= 0:
            while number >= 0:
                print(number, end=", ")
                number -= 1
        # Comportamiento creciente: el número es negativo, cuenta hasta 0.
        else:
            while number <= 0:
                print(number, end=", ")
                number += 1

    except ValueError:
        print("This is not a valid number.")
