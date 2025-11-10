# Brief: Simple interactive calculator that supports add, subtract, multiply, divide.
# Input: prompts user for an option and two numbers; validates numeric input.
# Flow: repeats until user chooses Quit (option 5). Each branch performs the chosen operation.
# Error handling: catches ValueError for invalid numeric input and asks again.

print("Welcome to the calculator")

while True:
    print("What would you like to do?")
    menu = "1. Addition (+) \n2. Subtraction (-) \n3. Multiplication (*) \n4. Division (/) \n5. Quit "
    response = input(menu)

    if response == "5":
        break
    try:
        number1 = float(input("Please enter the first number: "))
        number2 = float(input("Please enter the second number: "))
    except ValueError:
        print("Please enter a valid number")
        continue

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
    else:
        print("You did not enter a valid option")