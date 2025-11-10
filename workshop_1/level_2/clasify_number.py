# Brief: Classify a number as positive, negative or zero.
# Input: reads a number and handles non-numeric input with a message.
# Flow: repeats while the user confirms (press 'Y') to continue.

print("What kind of number is this?")

while True:
    try:
        number = float(input("Please enter a number: "))
        if number < 0:
            print("This number is negative")
        elif number > 0:
            print("This number is positive")
        else:
            print("This number is zero")
    except ValueError:
        print("This number is invalid")
        continue

    response = input("Would you like to continue? Press (Y) to continue: ").capitalize()
    if response != "Y":
        break
