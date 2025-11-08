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