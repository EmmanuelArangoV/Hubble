from service.inventory import Inventory
from service.product import Product
from persistence.archives import get_data, save_data
from service.validations import validate_string, validate_integer, validate_float

BRANDS = ["Dell", "Samsung", "Logitech", "HP", "Razer", "Apple", "Sony"]

def main_menu(inventory):
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Register Product")
        print("2. List Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Register Sale")
        print("6. List Sales")
        print("7. Reports")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_product(inventory)
        elif choice == '2':
            list_products(inventory)
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")

def register_product(inventory):
    try:
        name = validate_string(input("Product Name: "), "Product Name")

        print("Available Brands:", ", ".join(BRANDS))
        brand = validate_string(input("Brand: "), "Brand")
        if brand not in BRANDS:
            add_brand = input(f"Brand '{brand}' not found. Would you like to add it? (yes/no): ")
            if add_brand.lower() == 'yes':
                BRANDS.append(brand)
            else:
                print("Product registration cancelled.")
                return

        category = validate_string(input("Category: "), "Category")
        unit_price = validate_float(input("Unit Price: "), "Unit Price")
        quantity = validate_integer(input("Quantity in Stock: "), "Quantity")
        warranty = validate_integer(input("Warranty (months): "), "Warranty")

        product = Product(name, brand, category, unit_price, quantity, warranty)
        inventory.add_product(product.to_dict())
        print("Product registered successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def list_products(inventory):
    products = inventory.get_all_products()
    if not products:
        print("No products found.")
        return

    for product in products:
        print(f"Name: {product['name']}, Brand: {product['brand']}, Price: {product['unit_price']}, Stock: {product['quantity_in_stock']}")

if __name__ == "__main__":
    inventory_service = Inventory("inventory.csv")
    main_menu(inventory_service)
import csv
import os

def get_data(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            pass
        return []

    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_data(file_path, data):
    if not data:
        return

    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

