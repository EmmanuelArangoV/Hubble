# Brief: Generate and display the multiplication table for a user-provided integer.
# Loop: ask for a number, print its products from 0 to 10, then ask to continue.
# Error handling: non-integer input is caught and a message is shown.

print("Do you want to learn the multiplication table?")

while True:
    try:
        number = int(input("Enter the number to generate its multiplication table: "))
        for i in range(11):
            result = number * i
            print(f"{number} * {i} = {result}")

        response = input("Would you like to continue? Press Y to continue ").capitalize()
        if response != "Y":
            break
    except ValueError:
        print("This is not a valid number.")