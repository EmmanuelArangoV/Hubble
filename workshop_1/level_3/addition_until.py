# Brief: Continuously read integers and accumulate their sum until the user enters 0.
# Input: prompts for an integer, uses try/except to handle invalid input.
# Stop condition: loop ends when the entered number is exactly 0.

number = None
result = 0
while number != 0:
    try:
        number = int(input("Enter a number. (Write 0 to finalize): "))
        result += number
    except ValueError:
        print("Please enter a number.")
print(f"The result is: {result}")