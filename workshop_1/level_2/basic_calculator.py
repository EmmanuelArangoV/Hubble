print("Welcome to the calculator")

while True:
    try:
        number1 = float(input("Please enter the first number: "))
        number2 = float(input("Please enter the second number: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    print("What would you like to do?")
    menu = "1. Addition (+) \n2. Subtraction (-) \n3. Multiplication (*) \n4. Division (/) \n5. Quit"
    response = input(menu)

    if response == "1" or response == "+":
        result = number1 + number2
        print(f"The sum of {number1} + {number2} = {result}")
    elif response == "2" or response == "-":
        result = number1 - number2
        print(f"The difference of {number1} - {number2} = {result}")
    elif response == "3" or response == "*":
        result = number1 * number2
        print(f"The product of {number1} * {number2} = {result}")
    elif response == "4" or response == "/":
        result = number1 / number2
        print(f"The quotient of {number1} / {number2} = {result}")
    elif response == "5":
        print("Thanks for using this calculator")
        break
    else:
        print("Please enter a valid number")