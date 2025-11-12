# Import Product and Inventory classes
from user_story.week_2.product import Product
from user_story.week_2.inventory import Inventory

# Import pathlib so the path of the csv file could change no matter the directory or the pc
from pathlib import Path

# Making the path flexible
BASE_DIR = Path(__file__).resolve().parent
path = BASE_DIR / "inventory.csv"

# Menu of options
menu = ("Menu\n"
        "1. Add product to inventory\n"
        "2. Show inventory\n"
        "3. Calculate statistics\n"
        "4. Delete product from inventory\n"
        "5. Update quantity\n"
        "6. Exit\n")

# Initializing inventory with the csv file and loading the information with the method of the class Inventory
inventory = Inventory(path)

# Main loop of the program
while True:
    print("Welcome to Inventory Management System")
    menu_choice = input(menu)

    # Evaluating options
    if menu_choice == "1":

        # Option 1: Add one or more products to the inventory
        while True:
            try:
                # Read product details from user (accept comma as decimal separator)
                name = input("Enter product name: ").capitalize()
                price = input("Enter product price: ").replace(',', '.')
                quantity = input("Enter product quantity: ")

                # Create Product instance and add it to inventory
                product = Product(name, price, quantity)
                inventory.add_product(product)

            except ValueError as e:
                # Handle invalid input when creating Product
                print("Invalid input", e)

            # Ask if user wants to add another product; break loop if not
            subchoice = input("Would you like to add other product? Press 'Y' to continue:\n").capitalize()
            if subchoice != "Y":
                break

    elif menu_choice == "2":
        # Option 2: Display all products in the inventory
        print("This is the inventory")
        inventory.show_inventory()

    elif menu_choice == "3":
        # Option 3: Calculate and show inventory statistics
        print("Statistics of the inventory\n")
        inventory.statistics()

    elif menu_choice == "4":
        # Option 4: Remove a product by name
        product = input("Enter product name: ").capitalize()
        inventory.remove_product(product)

    elif menu_choice == "5":
        # Option 5: Update an existing product's details
        try:
            name = input("Enter product name: ").capitalize()
            price = input("Enter product price: ").replace(',', '.')
            quantity = input("Enter product quantity: ")

            # Build Product object and use it to update inventory entry
            product = Product(name, price, quantity)
            inventory.update_product(product)
        except ValueError as e:
            # Handle invalid input when creating Product for update
            print("Invalid input", e)

    elif menu_choice == "6":
        # Option 6: Exit the program loop
        print("Thanks for using the program!")
        break

    else:
        # Any other input is an invalid menu choice
        print("Invalid choice")