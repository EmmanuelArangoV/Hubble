# Brief: Compute the summation of integers from 1 to a positive limit entered by the user.
# Validation: require an integer greater than or equal to 1; invalid inputs are rejected.
# Output: print the total sum and ask the user whether to perform another calculation.

print("Welcome to summation!")

while True:
    try:
        number = int(input("What number will be your limit? "))
        summation = 0
        if number < 1:
            raise ValueError
        else:
            for i in range(1, number+1):
                summation += i
            print(f"The value of the summation from 1 to {number} is {summation}")

        response = input("Would you like to continue? Press Y to continue ").capitalize()
        if response != "Y":
            break
    except ValueError:
        print("This is not a valid number.")