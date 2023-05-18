#May 13, 2023 6:21pm
# I wanna make a program that kinda talks to you when getting your info

import sys
sys.path.append("E:/Programming/Python/My Projects/Python")
import typethis

def getInfo():
    
    def student_info():
       
        def education_level(check):
            
            if check == "Elementary" or check == "1":
                grade_level = int(input("What grade are you in? "))
                if 1 < grade_level > 6:
                    print("Elementary only has grades 1-6") 
            elif check == "Highschool" or check == "2":
                grade_level = int(input("What grade are you in? "))
                if 7 < grade_level > 10:
                    print("Highschool only has grades 7-10") 
            elif check == "Senior Highscool" or check == "3":
                grade_level = int(input("What grade are you in? "))
                if 11 < grade_level > 12:
                    print("Senior Highschool only has grades 11-12") 
            elif check == "College" or check == "4":
                grade_level = int(input("What grade are you in? "))
                if 1 < grade_level > 4:
                    print("College level has only 1-4 years at most") 
            
            return grade_level
        print("EDUCATIONAL BACKGROUND".center(40))
        counter = 1
        education = ("Elementary", 
                     "Highschool", 
                     "Senior Highschool", 
                     "College")
        for level in education:
            print(f"{counter}.{level}", end=", ")
            counter += 1
        print()
        choice = input("Select your current education: ")
        if choice.capitalize() in education or not (1 < int(choice) > 5):
            if not choice.isdigit(): 
                print(education_level(choice.capitalize))
            else:
                print(education_level(choice))
    
    
    student_info()
                

    def work_info():
        print("EMPLOYMENT BACKGROUND")


    name = input("Enter your name: ")
    birthdate = input("Enter your birthday(MM/DD/YYYY): ")
    gender = input("Enter your gender: ")
    status = input("Enter your status: ")
    student = input("Are you a student?(yes/no): ").lower()
    if student == "yes":
        student_info()
    else:
        work_info()
    

def main():
    getInfo()
    pass
def seeInfo():
    pass

main()
