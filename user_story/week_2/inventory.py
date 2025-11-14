# Import csv module to python for writing and reading operations
import csv

# Import class product
from user_story.week_2.product import Product

# Class Inventory
class Inventory:
    def __init__(self, path):
        self.path = path
        self.items = []
        self.load_from_csv()

    # Import the information from the csv file into a list
    def load_from_csv(self):
        try:
            with open(self.path, mode='r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product = Product(row['name'], row['price'], row['quantity'])
                    self.items.append(product)
        except FileNotFoundError:
            print("Inventory not found")
            self.items = []

    # Save the information from the list to the csv file overwriting the old information
    def save_to_csv(self):
        with open(self.path, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'price', 'quantity'])
            writer.writeheader()
            for item in self.items:
                writer.writerow(item.to_dict())

    # Search the new product's name in the list and if it's not we can append it to the list otherwise raise an error.
    def add_product(self, product):
        for item in self.items:
            if product.name == item.name:
                raise ValueError("Product already exists")

        self.items.append(product)
        print("Product added to inventory")
        self.save_to_csv()

    # Update product matching by name, it can only update price and quantity
    def update_product(self, product):
        for item in self.items:
            if product.name == item.name:
                item.price = product.price
                item.quantity = product.quantity
                print("Product updated successfully\n")
                self.save_to_csv()
                return True

        print("Product not found")
        return False

    # Remove product matching by name
    def remove_product(self, name):
        for item in self.items:
            if item.name == name:
                print("Product removed successfully")
                self.items.remove(item)
                self.save_to_csv()
                return True

        print("Product not found")
        return False

    # Show all the inventory through an iterative method if there's nothing in the list also print the exception
    def show_inventory(self):
        if len(self.items) == 0:
            print("There are no products in inventory")
        else:
            for item in self.items:
                print(f"Product: {item.name} | Price: {item.price} | Quantity: {item.quantity}")

    # Statistics of the inventory
    def statistics(self):
        if len(self.items) == 0:
            print("There are no products in inventory")
        else:
            total_price = 0
            total_quantity = 0
            for item in self.items:
                subtotal = item.price * item.quantity
                total_price += subtotal
                total_quantity += item.quantity
                print(f"Product: {item.name} | Quantity: {item.quantity} | Price: {item.price} | Subtotal: ${subtotal}")

            print(f"Total price of the inventory: ${total_price}\n")
            print(f"There are {len(self.items)} products in inventory")
            print(f"Total quantity units of the inventory: {total_quantity}\n")

    def product_available(self, name):
        if name == "":
            raise ValueError("Product name cannot be empty")
        for item in self.items:
            if item.name == name:
                raise ValueError("Product already exists")