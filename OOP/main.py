from Items import Item
from phone import Phone






item1 = Item("shake", 5000, 2)
item1.__name = "shakeitoff"
phone1 = Phone("sha", 100, 2, 1)
phone1.discounted_price()
print(phone1.price)