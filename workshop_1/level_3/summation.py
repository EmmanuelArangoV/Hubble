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