# isPositive: helper that returns True for positive ages.
# Main: prompt for name (non-empty) then prompt for age (positive integer).
# Validation: age input is validated using isPositive and exception handling.
# Output: greet the user with name and age, then ask whether to continue.

def isPositive(age):
    if age > 0:
        return True
    else:
        return False

print("Hello user, I hope you're having a great day")
while True:
    name = input("Enter your name: ")

    if name == "":
        print("Please enter a valid name")
        continue
    else:
        while True:
            try:
                age = int(input("Enter your age: "))
                if not isPositive(age):
                    raise ValueError
            except ValueError:
                print("Please enter a valid age")
                continue
            break

    print(f"Hello {name}, you are {age} years old")

    response = input("Would you like to continue. Press (Y) to continue: ").capitalize()
    if response != "Y":
        break