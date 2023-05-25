#May 20, 2023
#making a custom character using class

class Human:

    def __init__(self, name, job, status):
        self.name = name
        self.job = job
        self.status = status
        return 


count = input("How many humans do you want to input? ")
humans = []
for i in range(int(count)):
    profile, job, status = input("Enter your name, job, status:(must be separated with spaces) ").split()
    p = Human(profile, job, status)
    humans.append(p)

print(humans[0].job, humans[1].name)
print(len(humans))
