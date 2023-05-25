#May 25, 2023
#Simple OOP Program

import csv

class Item:
    #class attributes
    discount = 0.2
    all_items = []

    #instance attributes
    def __init__(self, name:str, price: float, quantity=1) -> None:
        #Validating the attributes using the asser

        assert price >= 0 , "The price is less than zero!"
        assert quantity >= 0, "The quantity is less than zero"
        #Attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        #append
        Item.all_items.append(self)


    #creating a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv') as f:
            reader = csv.DictReader(f)
            listed_item = list(reader)
        
        for instance in listed_item:
            Item (
                name=instance.get('name'),
                price=instance.get('price'),
                quantity=instance.get('quantity')
            )

    def getTotal(self):
        return self.price * self.quantity
    
    #return a string representation of the object
    def __repr__(self):
        return f"(Name: {self.name} Price: {self.price} Qty: {self.quantity})"
    

Item.instantiate_from_csv()    
print(Item.all_items)


