from item import Item
from keyboard import Keyboard

item1 = Item("MyItem", 750)

item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)

item2 = Keyboard("NewKeyboard", 1000, 3)

item2.apply_discount()


print(item2.price)