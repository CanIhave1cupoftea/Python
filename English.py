#May 10, 2023
# English subject with 5 words to be rearranged

import random

english_word = ["ingger", "elpap", "remobb", "yphpa", "eivrece", "twach", "cibsa"]
answers = ["ginger", "apple", "bomber", "happy", "receive", "watch", "basic"]
def english_sub():
    score = 0
    for word in range(5):
        random_word = english_word.pop(random.randint(0, len(english_word)-1))
        print(f"What word can you make with these jumbled letters? {random_word}")
        answer = input("Enter your answer: ")
        if answer.lower() in answers:
            score += 20
    return score


def english_remark():
    if quiz < 80:
        return "Failed"
    else:
        return "Passed" 
    

quiz = english_sub()
print(english_remark())

"""student_name = input("What is Your Name? ")
student_course = input("What is your course? ")
student_year = int(input("What is your year level? "))
student_age = int(input("What is your age? "))

student_data = {"Name" : student_name.capitalize(), "Course": student_course.upper(), "Year Level": student_year, "Age": student_age}
for key, value in student_data.items():
    print(f"{key}: {value}")"""