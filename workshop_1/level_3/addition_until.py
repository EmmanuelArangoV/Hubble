number = None
result = 0
while number != 0:
    try:
        number = int(input("Enter a number. (Write 0 to finalize): "))
        result += number
    except ValueError:
        print("Please enter a number.")
print(f"The result is: {result}")