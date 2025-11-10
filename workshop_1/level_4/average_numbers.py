# Brief: Collect numeric inputs in a list and allow listing or averaging them.
# Menu: 1=add number, 2=list numbers, 3=calculate average, 4=exit.
# Option 1: validate input as float and append to numbers.
# Option 2: iterate and print each stored number.
# Option 3: if list empty notify user; otherwise sum values and divide by count to get average.
# Option 4: exit the loop and end the program.

numbers = []
menu = "1. Add numbers.\n2. List numbers.\n3. Calculate average.\n4. Exit\n"

while True:
    choice = input(menu)
    if choice == "1":
        try:
            number = float(input("Enter number: "))
            numbers.append(number)
        except ValueError:
            print("Invalid number.")
    elif choice == "2":
        for number in numbers:
            print(number, end=", ")
    elif choice == "3":
        if len(numbers) == 0:
            print("No numbers entered.")
        else:
            average = 0
            for number in numbers:
                average += number
            result = average / len(numbers)
            print(f"The average of the numbers in the list is {result}.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
