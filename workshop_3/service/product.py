class Product:
    def __init__(self, name, brand, category, unit_price, quantity_in_stock, warranty_months):
        self.name = name
        self.brand = brand
        self.category = category
        self.unit_price = unit_price
        self.quantity_in_stock = quantity_in_stock
        self.warranty_months = warranty_months

    def to_dict(self):
        return {
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
            "unit_price": self.unit_price,
            "quantity_in_stock": self.quantity_in_stock,
            "warranty_months": self.warranty_months
        }

