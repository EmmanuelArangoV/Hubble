from service.product import Product

class Inventory:
    def __init__(self, file_path):
        self.products = []
        self.file_path = file_path
        self.load_products()

    def load_products(self):
        # This will be handled by the persistence layer
        pass

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product
        return None

    def update_stock(self, product_name, quantity):
        product = self.get_product(product_name)
        if product:
            product.quantity_in_stock -= quantity
            return True
        return False

    def get_all_products(self):
        return self.products

