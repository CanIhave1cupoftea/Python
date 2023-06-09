#Activity 1 python, June 1
"""class Worker:
    workers = []

    def __init__(self, role: str, name: str, age: int, emp_id: int) -> None:
        
        self.role = role
        self.name = name
        self.age = age
        self.empid = emp_id
        Worker.workers.append([self.role, self.name, self.age, self.empid])
        print()

    @classmethod
    def details(cls):
        for num, worker in enumerate(Worker.workers):
            print(f"Worker {num+1}")
            print(f"Role: {worker[0]}\nName: {worker[1]}\nAge: {worker[2]}\nEmployee ID: {worker[3]}")
            print()

def main():
    choice = int(input("How many workers do you want to input? "))
    for i in range(choice):

        role = input("Role: ")
        name = input("Name: ")
        age = input("Age: ")
        emp_id = input("Employee ID: ")
        W = Worker(role, name, age, emp_id)
main()
Worker.details()
"""


class Worker:
    workers = []

    def __init__(self, role: str, name: str, age: int, emp_id: int) -> None:
        
        self.role = role
        self.name = name
        self.age = age
        self.empid = emp_id
        Worker.workers.append([self.role, self.name, self.age, self.empid])
        print()

    @classmethod
    def details(cls):
        for num, worker in enumerate(Worker.workers):
            print(f"Worker {num+1}")
            print(f"Role: {worker[0]}\nName: {worker[1]}\nAge: {worker[2]}\nEmployee ID: {worker[3]}")
            print()

def main():
    choice = int(input("How many workers do you want to input? "))
    for i in range(choice):

        role = input("Role: ")
        name = input("Name: ")
        age = input("Age: ")
        emp_id = input("Employee ID: ")
        W = Worker(role, name, age, emp_id)
main()
Worker.details()