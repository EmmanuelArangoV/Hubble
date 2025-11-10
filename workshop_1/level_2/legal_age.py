# Brief: Check whether the entered age represents legal adulthood.
# Validation: ensures age is an integer and non-negative; handles invalid input.
# Flow: informs if minor or adult and repeats while the user confirms.

print("Are you of legal age?")
while True:
    try:
        age = int(input("What is your age? "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age < 18:
            print("You are a minor.")
        else:
            print("You are of legal age.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue

    response = input("Would you like to check another age? Press (Y) to continue: ").capitalize()
    if response != "Y":
        break