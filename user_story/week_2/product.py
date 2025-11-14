# Class product for the list
class Product:
    # Constructor of the class product with parameters; name, price, quantity
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name with validations
    @name.setter
    def name(self, value):
        self._name = value

    # Getter for price
    @property
    def price(self):
        return self._price

    # Setter for price with validations
    @price.setter
    def price(self, value):
        try:
            value = float(value)
            if value <= 0:
                raise ValueError("Price cannot be negative or zero")
        except:
            raise ValueError("Price should be an integer or decimal value")
        self._price = value

    # Getter for quantity
    @property
    def quantity(self):
        return self._quantity

    # Setter for quantity with validations
    @quantity.setter
    def quantity(self, value):
        try:
            value = int(value)
            if value <= 0:
                raise ValueError("Quantity cannot be negative or zero")
        except:
            raise ValueError("Quantity should be an integer value")

        self._quantity = value

    # Method to convert an object of the class product to a dictionary, used to insert a new register in the csv file
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
        }