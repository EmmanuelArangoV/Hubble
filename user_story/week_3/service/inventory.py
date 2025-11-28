from user_story.week_3.service.product import *
from user_story.week_3.service.validations import *

class Inventory:
    def __init__(self):
        self.items = []
        self.persistence = True

    def add_product(self, name: str, price: float, quantity: int):
        if not self.name_available(name):
            raise ValueError(ctext(f"Product name '{name}' is already in use.", 'error'))
        product = Product(name, price, quantity)
        self.items.append(product)
        self.persistence = False
        print(ctext(f"Product '{name}' added.", 'success'))

    def show_inventory(self):
        if not self.items:
            print(ctext("Inventory is empty.", 'warning'))
            return
        for i, item in enumerate(self.items, start=1):
            print(ctext(f"{i}. Product: {item.name} | Price: ${item.price} | Quantity: {item.quantity} | Subtotal: ${item.price * item.quantity}", 'info'))

    def search_product(self, name: str, filter=None):
        if not self.items:
            print(ctext("Inventory is empty.", 'warning'))
            return None
        products = []
        if filter is not None:
            return self.search_product_partial(name)
        else:
            for item in self.items:
                if name == item.name:
                    products.append(item)
        return products or None

    def search_product_partial(self, name: str):
        products = []
        for item in self.items:
            if name in item.name:
                products.append(item)
        return products or None

    def update_product(self, name: str, price=None, quantity=None):
        update = False
        for item in self.items:
            if name == item.name:
                item.price = price if price is not None else item.price
                item.quantity = quantity if quantity is not None else item.quantity
                print(ctext(f"Product {name} updated successfully.", 'success'))
                update = True
                self.persistence = False
        if not update:
            print(ctext(f"Product {name} not found in inventory.", 'error'))

    def delete_product(self, name: str):
        delete = False
        for item in self.items:
            if name == item.name:
                self.items.remove(item)
                print(ctext(f"Product {name} deleted successfully.", 'success'))
                delete = True
                self.persistence = False
        if not delete:
            print(ctext(f"Product {name} not found in inventory.", 'error'))

    def total_units(self):
        total_quantity = 0
        for item in self.items:
            total_quantity += item.quantity
        return total_quantity

    def total_value(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def most_expensive_product(self):
        if not self.items:
            return None
        else:
            return max(self.items, key=lambda item: item.price)

    def most_stocked_product(self):
        if not self.items:
            return None
        else:
            return max(self.items, key=lambda item: item.quantity)

    def statistics(self):
        stats = {
            "total_units": self.total_units() if self.items is not None else "N/A",
            "total_value": self.total_value() if self.items is not None else "N/A",
            "most_expensive_product": self.most_expensive_product() if self.items is not None else "N/A",
            "most_stocked_product": self.most_stocked_product() if self.items is not None else "N/A"
        }
        return stats

    def name_available(self, name: str) -> bool:
        for item in self.items:
            if name == item.name:
                return False
        return True

    def is_valid_input(self, name: str, price: str, quantity: str) -> bool:
        try:
            valid_string(name)
            parse_positive_float(price)
            parse_positive_int(quantity)
            return True
        except ValueError as e:
            print(ctext(f"Input validation error: {e}", 'error'))
            return False