# Brief: Collect three numbers and report the largest and smallest.
# Input: prompts until three valid floats are entered; invalid inputs are rejected.
# Logic: iterates to find biggest and smallest values among the collected numbers.
# Flow: allows repeating the process while the user chooses to continue.
print ("Welcome to the Number Comparator")

while True:
    numbers = []
    while len(numbers) < 3:
        try:
            number = float(input(f"Enter the number {len(numbers)+1}: "))
            numbers.append(number)
        except ValueError:
            print("Enter a valid number")


    biggest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > biggest:
            biggest = number
        elif number < smallest:
            smallest = number

    print(f"The biggest number is: {biggest}")
    print(f"The smallest number is: {smallest}")

    response = input("Would you like to try another round? Press (Y) to continue: ").capitalize()

    if response != "Y":
        break