#May 25, 2023
#Simple OOP Program

import csv

class Item:
    #class attributes
    discount = 0.8
    all= []

    #instance attributes
    def __init__(self, name:str, price: float, quantity=1) -> None:
        #Validating the attributes using the asser

        assert price >= 0 , "The price is less than zero!"
        assert quantity >= 0, "The quantity is less than zero"
        #Attributes
        self.__name = name
        self.price = price
        self.quantity = quantity

        #append
        Item.all.append(self)

    #getter
    @property # - transforms a method into a property, making it act like a read-only attribute
    def name(self):
        return self.__name

    #setter
    @name.setter
    def name(self, new):
        self.__name = new
    

    #creating a class method
    @classmethod #- a class method is a function that receive the class name as an argument rather than the instance
    def instantiate_from_csv(cls):
        with open('OOP\item.csv') as f:
            reader = csv.DictReader(f)
            listed_item = list(reader)
        
        for instance in listed_item:
            Item (
                instance.get('name'),
                float(instance.get('price')),
                int(instance.get('quantity'))
            )

    
    
    #codes that start with @ are called decorators
    #creating a static method
    @staticmethod  # - static method is somethig that does instantiate or refer to itself when called, unlike class and instance functions/methods
    def is_integer(num):

        if isinstance(num, float):
            return int
        elif isinstance(num, int):
            return True
        else:
            return False
        


    def getTotal(self):
        return self.price * self.quantity
    

    def discounted_price(self):
        self.price = self.price * self.discount

    #return a string representation of the object
    def __repr__(self):
        return f"{self.__class__.__name__}(Name: {self.name} Price: {self.price} Qty: {self.quantity})"
    
    


Item.instantiate_from_csv()    




