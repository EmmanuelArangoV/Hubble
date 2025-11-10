# Interactive menu to show how input is interpreted as different Python types.
# Menu: options map to conversions for int, float, string, bool, list, or exit.
# Validation: numeric conversions use try/except; list input is split by commas.
# Note: boolean conversion here uses Python bool() on the input string.

menu = "1. Integer \n2. Float \n3. String \n4. Boolean \n5. List \n6. Exit\n"

while True:
    print("Hi! Welcome to the Variable Type Explorer")
    print("Please select how do you want to treat your input:")
    option = input(menu)

    match option:
        case "1":
            try:
                user_input = int(input("Please enter a number: "))
                print (f"You have entered an Integer: {user_input} of type {type(user_input)}")
            except ValueError:
                print("Invalid input. Please enter a valid Integer.")
        case "2":
            try:
                user_input = float(input("Please enter a number: "))
                print (f"You have entered a Float: {user_input} of type {type(user_input)}")
            except ValueError:
                print("Invalid input. Please enter a valid Float.")
        case "3":
            user_input = input("Please enter a text: ")
            print (f"You have entered a String: '{user_input}' of type {type(user_input)}")
        case "4":
            try:
                user_input = bool(input("Please enter True or False: ").capitalize())
                print (f"You have entered a Boolean: {user_input} of type {type(user_input)}")
            except ValueError:
                print("Invalid input. Please enter True or False.")
        case "5":
            print("Please enter multiple values separated by commas:")
            user_input = input().split(",")
            print (f"You have entered a List: {user_input} of type {type(user_input)}")
        case "6":
            print("Exiting the Variable Type Explorer. Goodbye!")
            break
        case _:
            print("Invalid option. Please select a valid option from the menu.")