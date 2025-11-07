# Creation of de the inventory with data type dictionary
inventory = {}

# Creation of the menu
menu = "Menu\n1. Add product to inventory.\n2.Calculate total cost.\n3. Show Inventory.\n4.Update Quantity.\n5.Exit.\n"

# Method to add products to the inventory
def addInventory():
    enter = "Y"

    # 1. Request for product data to the user
    while enter == "Y":
        # 1.1. Validate that the product name is unique
        while True:
            productName = input("Enter the name of the product for inventory: ").capitalize()
            if productName in inventory:
                print("The product already exists in the inventory. Please enter a unique name.")
            elif productName == "":
                print("You have entered an empty product name. Please enter a valid product name.")
            else:
                break

        # 1.2. Validate that the price is a number and positive
        while True:
            try:
                productPrice = float(input("Enter the price of the product for inventory: ").replace(",","."))
                if not isPositive(productPrice):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("You have entered and invalid value for the price of the product. Please make sure is a positive number, greater than zero.")

        # 1.3. Validate that the quantity is a number and positive, if it's not, make an exception
        productQuantity = getIntNumber()

        inventory[productName] = {"price": productPrice, "quantity": productQuantity}

        enter = input("Do you wish to continue adding products to the inventory? (Y/N): ").upper()


# Method to check if a number is positive
def isPositive(number):
    return number > 0

# Method to make sure we get a data type int greater than zero
def getIntNumber():
    while True:
        try:
            productQuantity = int(input("Enter the quantity of the product for inventory: "))
            if not isPositive(productQuantity):
                raise ValueError
            else:
                break
        except ValueError:
            print("You have entered and invalid value for the quantity of the product. Please make sure is a positive number, greater than zero.")
    return productQuantity

# Method to calculate the total cost of a product
def calculateTotalCost(product):
    if not product in inventory:
        print("The product does not exist in the inventory. Please enter a valid product name.")
        return None
    total_cost = inventory[product]["price"] * inventory[product]["quantity"]
    return total_cost

# Method to show the result of the product's total cost
def showResult(product, totalCost):
    print(f"Product: {product} | Price: {inventory[product]['price']} | Quantity: {inventory[product]['quantity']} | Total Cost: ${totalCost}")

# Method to show the inventory
def showInventory():
    for product in inventory:
        print(f"Product: {product} | Price: {inventory[product]['price']} | Quantity: {inventory[product]['quantity']}")

# Method to update the quantity in stock of a product
def updateInventory():
    productName = input("Enter the name of the product to update: ").capitalize()
    if productName in inventory:
        productQuantity = getIntNumber()
        inventory[productName]["quantity"] = productQuantity
    else:
        print("The product does not exist in the inventory.")

if __name__ == "__main__":
    while True:
        option = input(menu)
        match option:
            case "1":
                addInventory()
            case "2":
                product = input("Enter the name of the product in the inventory: ").capitalize()
                totalCost = calculateTotalCost(product)
                if totalCost is not None:
                    showResult(product, totalCost)
            case "3":
                showInventory()
            case "4":
                updateInventory()
            case "5":
                print("Thanks for using the program.")
                break
            case _:
                print("Invalid option. Please enter a valid option.")

# General comment:
# This program manages a temporal inventory using the 'inventory dictionary.
# It provides an interactive menu to:
# - Add products with validation for unique name, positive price, and positive quantity
# - Calculate and display the total cost for a selected product.
# - Show all products in the current inventory.
# - Update the quantity of an existing product.
# The input that the user makes is validated with some extra functions ('isPosititve', 'getIntNumber').
# All data is lost when the program exits.