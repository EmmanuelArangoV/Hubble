from os import remove

numbers = []
menu = "1. Add numbers.\n2. Show numbers.\n3. Eliminate duplicates\n4. Exit\n"

while True:
    choice = input(menu)
    if choice == "1":
        try:
            number = int(input("Enter your number: "))
            if number % 2 == 0:
                numbers.append(number)
            else:
                print("That is not an even number.")
        except ValueError:
            print("Invalid number.")
    elif choice == "2":
        for number in numbers:
            print(number, end=", ")
        print()
    elif choice == "3":
        for i in numbers:
            new_numbers = numbers.copy()
            new_numbers.remove(i)
            for j in new_numbers:
                if j == i:
                    numbers.remove(j)
        print("Duplicates numbers were removed.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")