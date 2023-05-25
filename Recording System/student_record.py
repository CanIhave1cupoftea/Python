#May 11, 2023 5:55pm
#May 13, 2023 - continued

class Student:

    def getStudent(self):
        
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade Level: ")

    def __init__(self, name, age, grade_level, subjects) -> None:
        self.name = name
        self.age = age
        self.grade = grade_level
        self.sub = [{"Grade 7": ("Science", "Math", "Filipino", "Esp")},
                    {"Grade 8": ("Science", "Math", "English", "Filipino", "EsP")},
                    {"Grade 9": ("Araling Panlipunan", "Math", "English", "Filipino")},
                    {"Grade 10": ("Calculus", "English", "Araling Panlipunan: Economics")}
                    ]

    def seeInfo(self):

        return self.sub
    

S = Student()
real = S.getStudent()
        