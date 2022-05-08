from asyncore import read
import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Run validations to the received arguments
        assert quantity >= 0, (
            f"Quantity {quantity} is not greater or equal to zero")
        assert price >= 0, (f"Price {price} is not greater than zero")

        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

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
        return (f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})")

class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods  
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, (f"Broken Phones {broken_phones} is not greter or equal to zero")
        
        self.broken_phones = broken_phones

    
phone1 = Phone("Phone1", 500, 5, 1)

print(Item.all)
print(Phone.all)
