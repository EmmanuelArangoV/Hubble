print("Welcome to regressive counter.")

while True:
    try:
        number = int(input("Please enter the number: "))
        if number >= 0:
            while number >= 0:
                print(number, end=", ")
                number -= 1
        else:
            while number <= 0:
                print(number, end=", ")
                number += 1

    except ValueError:
        print("This is not a valid number.")
