# Brief: Print numbers from 1 up to a given limit; allow changing the limit and repeating.
# Initial behavior: counts from 1 to 10, then asks the user whether to continue.
# Update: if continuing, prompt for a new upper bound and validate it as an integer.
# Error handling: invalid numeric input is handled with try/except and a message.

print("We're gonna count from 1 to 10")

number = 10
while True:
    for i in range(number):
        print(f"Number: {i+1}")

    response = input("Would you like to continue. Press (Y) to continue: ").capitalize()
    if response != "Y":
        break
    else:
        while True:
            try:
                number = int(input("Until what number would you like to count: "))
                break
            except ValueError:
                print("Please enter a valid number for the counting.")