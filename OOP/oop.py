#May 20, 2023

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello my name is {self.name} and my age is {self.age}"
    
class Animals:

    def __init__(self, name, animal) -> None:
        self.name = name
        self.animal = animal

    def eat(self):

        print("I am now eating")


personOne = Person("Pacis", 20)
personTwo = Person("Ced", 22)
print(personOne.introduce())
print(personTwo.introduce())

animalOne = Animals("Jake", "Dog")
print(animalOne.eat())