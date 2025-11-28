import csv
from typing import List
from user_story.week_3.service.inventory import Inventory
from user_story.week_3.service.validations import ctext

class fileCSV:
    def __init__(self, path: str):
        self.path = path

    def save_csv(self, inventory: Inventory):
        if not inventory.items:
            print(ctext("Inventory is empty. Nothing to save.", 'warning'))
            return
        try:
            with open(self.path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'price', 'quantity'])
            self.save_content_csv(inventory)
        except PermissionError:
            raise PermissionError("You do not have permission to create the file at the specified path.")
        except Exception as e:
            raise e


    def save_content_csv(self, inventory: Inventory):
        try:
            with open(self.path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for item in inventory.items:
                    writer.writerow([item.name, item.price, item.quantity])
            inventory.persistence = True
            print(ctext(f"Inventory saved successfully to {self.path}.", 'success'))
        except PermissionError:
            raise PermissionError("You do not have permission to write to the file at the specified path.")
        except Exception as e:
            raise e

    def load_csv(self, inventory: Inventory, overwrite=True):
        errors = 0
        if overwrite:
            try:
                inventory.items.clear()
                with open(self.path, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader, None)  # skip header if present
                    for row in reader:
                        if len(row) != 3:
                            continue
                        name, price, quantity = row
                        if inventory.is_valid_input(name, price, quantity):
                            inventory.add_product(name, float(price), int(quantity))
                        else:
                            errors += 1
            except FileNotFoundError:
                # No file yet; start with empty inventory
                return inventory
        else:
            inventory = self.fusion_csv(inventory)
        inventory.persistence = False
        print(ctext(f"Inventory loaded successfully from {self.path}. Invalid rows: {errors}", 'info'))
        return inventory

    def fusion_csv(self, inventory: Inventory) -> Inventory:
        print(ctext("It will only update quantities of existing products and add new products.", 'info'))
        with open(self.path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                self.merge_row(inventory, row)
        inventory.persistence = False
        print(ctext(f"Inventory merged successfully from {self.path}.", 'success'))
        return inventory

    def merge_row(self, inventory: Inventory, row: List[str]) -> None:
        name, price, quantity = row
        products = inventory.search_product(name, filter=None)
        if products:
            for p in products:
                p.quantity += int(quantity)
        else:
            inventory.add_product(name, float(price), int(quantity))