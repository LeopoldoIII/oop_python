import csv

class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Run validations to the received arguments
        assert quantity >= 0, (
            f"Quantity {quantity} is not greater or equal to zero")
        assert price >= 0, (f"Price {price} is not greater than zero")

        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # Property decorator = Read-Onl y Attribute
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception("The Name is to Long!")
        self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    '''
    This should also do something that has a relationship with the class
    but usually, those are use to manipulate different structures of data to instantiate objects
    like we have done with CSV
    '''
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )
    '''
    This should do something that has a relationship
    with the class, but not something that must be unique
    per instance 
    
    '''
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are poit zero
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})")
