# add: return sum of two numbers
def add(a, b):
    return a + b

# subtract: return difference a - b
def subtract(a, b):
    return a - b

# multiply: return product of two numbers
def multiply(a, b):
    return a * b

# power: return a raised to the power n
def power(a, n):
    return a ** n

# divide: return a / b, or ValueError object when b is zero
def divide(a, b):
    if b == 0:
        return ValueError("Division by zero")
    return a / b

# root: return the n-th root of a, or ValueError when n is zero
def root(a, n):
    if n == 0:
        return ValueError("n-esim root cannot be zero.")
    return a ** (1/n)

# factorial: recursive factorial, expects non-negative integer
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return ValueError("It cannot be a negative number.")
    elif not n.is_integer():
        return ValueError("It cannot be a decimal number.")
    else:
        return n * factorial(n-1)

# mod: return a modulo b, or ValueError when b is zero
def mod(a, b):
    if b == 0:
        return ValueError("You cannot divide by zero")
    return a % b

# percent: calculate b percent of a
def percent(a, b):
    if b == 0:
        return 0
    return (a / 100) * b

# average: return arithmetic mean of a list of numbers
def average(list):
    return sum(list) / len(list)

# isNumber: try to convert input to float, return float or None on failure
def isNumber(num):
    try:
        num = float(num)
        return num
    except ValueError:
        print("Please enter a valid number.")
        return None

# menu: text shown to the user
menu = (""
        "1. Addition\n" "2. Subtraction\n" "3. Multiplication\n" "4. Division\n"
        "5. Power\n" "6. Root\n" "7. Factorial\n" "8. Modul\n" "9. Percent\n" "10. Average\n"
        "11. Exit\n")

# main loop: interact with the user until exit
while True:
    print("Welcome to Advanced Calculator")
    choice = input(menu)
    if choice == "1":
        a = isNumber(input("Enter the first number: "))
        b = isNumber(input("Enter the second number: "))
        if a is not None and b is not None:
            print(f"The result of the addition is of {a} and {b}: {add(a, b)}")
    elif choice == "2":
        a = isNumber(input("Enter the first number: "))
        b = isNumber(input("Enter the second number: "))
        if a is not None and b is not None:
            print(f"The result of the subtraction of {b} from {a}: {subtract(a, b)}")
    elif choice == "3":
        a = isNumber(input("Enter the first number: "))
        b = isNumber(input("Enter the second number: "))
        if a is not None and b is not None:
            print(f"The result of the multiplication of {a} and {b}: {multiply(a, b)}")
    elif choice == "4":
        a = isNumber(input("Enter the first number: "))
        b = isNumber(input("Enter the second number: "))
        if a is not None and b is not None:
            result = divide(a, b)
            if isinstance(result, ValueError):
                print(result)
            else:
                print(f"The result of the division of {a} by {b}: {result}")
    elif choice == "5":
        a = isNumber(input("Enter the base number: "))
        n = isNumber(input("Enter the exponent number: "))
        if a is not None and n is not None:
            print(f"The result of {a} raised to the power of {n}: {power(a, n)}")
    elif choice == "6":
        a = isNumber(input("Enter the number: "))
        n = isNumber(input("Enter the n-esim root: "))
        if a is not None and n is not None:
            result = root(a, n)
            if isinstance(result, ValueError):
                print(result)
            else:
                print(f"The result of the {n}-esim root of {a}: {result}")
    elif choice == "7":
        n = isNumber(input("Enter the number: "))
        if n is not None:
            result = factorial(n)
            if isinstance(result, ValueError):
                print(result)
            else:
                print(f"The factorial of {int(n)} is: {result}")
    elif choice == "8":
        a = isNumber(input("Enter the first number: "))
        b = isNumber(input("Enter the second number: "))
        if a is not None and b is not None:
            result = mod(a, b)
            if isinstance(result, ValueError):
                print(result)
            else:
                print(f"The result of the modul of {a} by {b}: {result}")
    elif choice == "9":
        a = isNumber(input("Enter the base number: "))
        b = isNumber(input("Enter the percentage number: "))
        if a is not None and b is not None:
            print(f"The result of the {b}% of {a}: {percent(a, b)}")
    elif choice == "10":
        numbers = []
        while True:
            num = isNumber(input("Enter a number to add to the list: "))
            if num is not None:
                numbers.append(num)
            answer = input("Do you want to add another number? Press (Y) to continue: ").capitalize()
            if answer != "Y":
                break
        if len(numbers) > 0:
            print(f"The average of the numbers {numbers} is: {average(numbers)}")
        else:
            print("There are no numbers to calculate the average.")
    elif choice == "11":
        print("Thank you for using Advanced Calculator. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid operation.")