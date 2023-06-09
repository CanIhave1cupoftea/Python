class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and my age is {self.age}")   

    def study(self):
        print("Studying...")

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print(f"Goodday! I am {self.name}, I'm {self.age} years old from {self.grade}!!.")

    def study(self):
        print("Studying for exams...")

class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"Goodday! I am {self.name}, I'm {self.age} and I am teaching {self.subject}.")

    def study(self):
        print("Currently preparing lesson plans")

class Principal(Person):

    def introduce(self):
        super().introduce()
        print("I am the head of this school")

    def study(self):
        print("Currently reviewing school policies")