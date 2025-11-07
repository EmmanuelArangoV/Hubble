print("Welcome to Calculator (only for addition)")

while True:
    try :
        number1 = float(input("Please enter a number:"))
        number2 = float(input("Please enter a number:"))
    except ValueError:
        print("Please enter valid numbers")
        continue

    addition = number1 + number2
    print(f"The result of adding {number1} and {number2} is: {addition}")

    response = input("Would you like to continue. Press (Y) to continue: ").capitalize()
    if response != "Y":
        break