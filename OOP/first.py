#May 14, 2023
#May 6:55am - continuation 
#First time tackling about classes and OOP in Python
"""
class Person:
    #this initiates the class to have attributes and methods

    #attributes
    conscious = True #class variable
    #initialization of attributes
    def __init__(self, name, age, gender):
        self.name = name        #instance variable
        self.age = age          #instance variable
        self.gender = gender    #instance variable

    #methods
    def walk(self):
        print(f"{self.name} is walking...")
    
    def run(self):
        print(f'{self.name} is running...')



human = Person("Henry", 21, "M")
print(human.name)
print(human.age)
print(human.gender)
print(human.conscious)

human.walk()
human.run()"""

#inheritance
#Grandparent class
class Organism:

    animal = f"This is alive"

#Parent class
class Animal(Organism):

    alive = True

    def eat(self):
        print(f"This is eating")
        return self
    
#Children class
"""class Dog(Animal):

    def bark(self):
        print("This dog barks")
        return self
        
class Cat(Animal):
    
    def meow(self):
        print("This cat meows")
        return self

class Lion(Animal, Organism):
    
    def roar(self):
        print("This lion roars!")
        return self

dog = Dog()
cat = Cat()
lion = Lion()

dog.bark()
cat.meow()
lion.roar()
lion.eat()
print(lion.alive)
print(lion.animal)
"""

#Abstraction
#In order to prevent the user from making an object from a class, we have to use abstraction
#when a method inside a class is abstracted it cannot be used by the user and the class directly but it can be used b the class' children and laso required to do so
#an abtract class has one or more abstract method, an abstract method is a method that has a declaration without an implementation

"""from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("this Car started")

class Motor(Vehicle):
    def start(self):
        print("THis morot started")

        vehicle = vehice
car = Car()
motor = Motor()
car.start()
motor.start"""

#we will try to make objects as argument

"""class Food:
    name = None

def change_name(name, new_name):
    
    name.name = new_name

food_1 = Food()
food_2 = Food()
print(food_1.name)
change_name(food_2, "adobo")
change_name(food_1, "sinigang")

print(food_1.name)"""

class Sample:

    #class variable/attribute
    text = "word"

    #instantiates and object
    def __init__(self, name) -> None:
        
        #instance variable
        self.name = name

    #instance method
    def sayHI(self):
        print("HI")

sample1 = Sample("this is an example")
print(sample1.name)
sample1.sayHI()