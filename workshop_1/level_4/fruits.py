fruits = ["Apple", "Banana", "Cherry"]
menu = "1. Add fruit.\n2.Delete fruit.\n3. Search fruit.\n4. Exit\n"

while True:
    choice = input(menu)
    if choice == "1":
        fruit = input("Enter fruit name: ").capitalize()
        if fruit not in fruits:
            fruits.append(fruit)
        else:
            print("The fruit you entered is already present.")
    elif choice == "2":
        fruit = input("Enter fruit name: ").capitalize()
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print("The fruit you entered doesn't seem to be present.")
    elif choice == "3":
        fruit = input("Enter fruit name: ").capitalize()
        #Old way
        for i in range(len(fruits)):
            if fruits[i] == fruit:
                print(f"The fruit {fruit} present.")
            elif i == len(fruits) - 1:
                print(f"The fruit {fruit} doesn't exist.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid choice.")