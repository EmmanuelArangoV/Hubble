print("An odd or even number?")

while True:
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")
    except ValueError:
        print("Please enter a valid number")
        continue

    response = input("Would you like to continue? Press (Y) to continue:").capitalize()
    if response != "Y":
        break