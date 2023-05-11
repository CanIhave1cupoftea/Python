#May 10, 2023
#Make student dictionary

students = {}
#getting student info
def student():
    print("\n\033[91m=====Enter STUDENT INFO=====\033[0m\n")
    s_id = int(input("ID: "))
    s_name = input("Name: ")
    s_course = input("Course: ")
    s_year = int(input("Year Level: "))
    s_age = int(input("Age: "))
    s_math = "No Remarks Yet"
    s_eng = "No Remarks Yet"
    s_fil = "No Remarks Yet"
    subjects = { "Math": 
            {   "CC": "MATH201",
                "CD": "Calculus",
                "TD": "2-5pm|Fri-Sat",
                "Room": "ComLab",
                "Instructor": "Ricardo Mallari"},
                
                "English": 
             {  "CC": "ENG201",
                "CD" : "Learning English",
                "TD": "9-11am|Mon-Tue",
                "Room": "DB 201",
                "Instructor": "Conrad Buerkley"}, 

                "Filipino":
            {   "CC": "FIL201",
                "CD": "Pag-aaral ng Filipino",
                "TD": "11-1pm|Wed-Thu",
                "Room": "MB 205",
                "Instructor": "Charmaine Dungca"},

            }
            

    if 1 < s_year > 5:
        print("That was way too low or high") 
    elif s_year == 1:
        s_year = "1st"
    elif  s_year == 2:
        s_year = "2nd"
    elif s_year == 3:
        s_year = "3rd"
    elif s_year == 4:
        s_year = "4th"

    return {
        "ID" : s_id,
        "Name" : s_name.capitalize(),
        "Course" : s_course.upper(),
        "Year": s_year,
        "Age": s_age,
        "Subjects" : {"Math":s_math, "English": s_eng, "Filipino": s_fil},
        "subjects_course" : subjects
    }
#math sub, odd and even
def math_sub():
    num = int(input("Enter a number: "))
    if 1 < num > 100:
        print("The number should not be less than 1 or greater than 100")
    def factorial(num=num): 
        numbers = [i for i in range(num, 0, -1)]
        product = 1
        for i in numbers:
            product *= i
        return f"{num}! is {product}"
    
    def odd_or_even(num=num):
        even = 0
        odd = 0
        for i in range(1, num+1):

            if i % 2 == 0:
                even += 1
            else:
                odd +=1
        return f"Even: {even}, Odd: {odd}"
    
    def prime_number(num=num):
        factors = 1
        if num > 1:
            for i in range(2, num+1):
                if num % i == 0:
                    factors += 1
        return f"{num} Is not a Prime Number" if factors > 2 else f"{num} Is a Prime Number"
    

    return f"{factorial(num)}, {odd_or_even(num)}, {prime_number(num)}"

#english sub
english_word = ["ingger", "elpap", "remobb", "yphpa", "eivrece"]
answers = ["ginger", "apple", "bomber", "happy", "receive"]
def english_sub():   
    score = 0
    for word in english_word:
        print(f"What word can you make with these jumbled letters? {word}")
        answer = input("Enter your answer: ")
        if answer.lower() in answers:
            score += 20
    
    return score, "Failed" if score < 80 else "Passed"
english_words = ["brave", "sharp", "dog", "banana", "king"]
filipino_answers = ["matapang", "matulis", "aso", "saging", "hari"]

def filipino_sub():
    score = 0
    for word in english_words:
        print(f"Translate this word -{word}- ")
        answer = input("Enter your answer: ")
        if answer.lower() in filipino_answers:
            score += 20
    return score, "Failed" if score < 80 else "Passed"

def see_student_info(num):
        
    print(f"Student ID: {students[num]['ID']}")
    print(f"Student Name: {students[num]['Name']}")
    print(f"Student Course: {students[num]['Course']}")
    print(f"Student Year-Level: {students[num]['Year']}")
    print(f"Student Age: {students[num]['Age']}")
    print(f"""Subjects:
    Math: {students[num]['Subjects']['Math']}
    English: {students[num]['Subjects']['English']}
    Filipino: {students[num]['Subjects']['Filipino']}""")

def subject_view(num):
        counter = 0
        for sub in students[num]["subjects_course"]:
            print(f"{counter+1}. {sub}")
            counter += 1
        print("---ALL---")
        print("--Exit--")
        sub_choice = input("Which Subject? ")
        if sub_choice == "1" or sub_choice.lower() == "math":
            print("\nMath:")
            print(f"Course Code: {students[num]['subjects_course']['Math']['CC']}")
            print(f"Course Description: {students[num]['subjects_course']['Math']['CD']}")
            print(f"Time & Day: {students[num]['subjects_course']['Math']['TD']}")
            print(f"Room: {students[num]['subjects_course']['Math']['Room']}")
            print(f"Instructor: {students[num]['subjects_course']['Math']['Instructor']}")
            print(f"Remarks: {students[num]['Subjects']['Math']}")
        elif sub_choice == "2" or sub_choice.lower() == "english":
            print("English:")
            print(f"Course Code: {students[num]['subjects_course']['English']['CC']}")
            print(f"Course Description: {students[num]['subjects_course']['English']['CD']}")
            print(f"Time & Day: {students[num]['subjects_course']['English']['TD']}")
            print(f"Room: {students[num]['subjects_course']['English']['Room']}")
            print(f"Instructor: {students[num]['subjects_course']['English']['Instructor']}")
            print(f"Remarks: {students[num]['Subjects']['English']}")
        elif sub_choice == "3" or sub_choice.lower() == "filipino":
            print("Filipino:")
            print(f"Course Code: {students[num]['subjects_course']['Filipino']['CC']}")
            print(f"Course Description: {students[num]['subjects_course']['Filipino']['CD']}")
            print(f"Time & Day: {students[num]['subjects_course']['Filipino']['TD']}")
            print(f"Room: {students[num]['subjects_course']['Filipino']['Room']}")
            print(f"Instructor: {students[num]['subjects_course']['Filipino']['Instructor']}")
            print({students[num]['Subjects']['Filipino']})
        elif sub_choice.lower() == "all":
            print("Math:")
            print(f"Course Code: {students[num]['subjects_course']['Math']['CC']}")
            print(f"Course Description: {students[num]['subjects_course']['Math']['CD']}")
            print(f"Time & Day: {students[num]['subjects_course']['Math']['TD']}")
            print(f"Room: {students[num]['subjects_course']['Math']['Room']}")
            print(f"Instructor: {students[num]['subjects_course']['Math']['Instructor']}\n")
            print("English:")
            print(f"Course Code: {students[num]['subjects_course']['English']['CC']}")
            print(f"Course Description: {students[num]['subjects_course']['English']['CD']}")
            print(f"Time & Day: {students[num]['subjects_course']['English']['TD']}")
            print(f"Room: {students[num]['subjects_course']['English']['Room']}")
            print(f"Instructor: {students[num]['subjects_course']['English']['Instructor']}\n")
            print("Filipino:")
            print(f"Course Code: {students[num]['subjects_course']['Filipino']['CC']}")
            print(f"Course Description: {students[num]['subjects_course']['Filipino']['CD']}")
            print(f"Time & Day: {students[num]['subjects_course']['Filipino']['TD']}")
            print(f"Room: {students[num]['subjects_course']['Filipino']['Room']}")
            print(f"Instructor: {students[num]['subjects_course']['Filipino']['Instructor']}\n")
        elif sub_choice.lower() == 'exit':
            return f"exit"
while True:
    student_num = int(input("How many students would you like to input? "))
    if student_num > 20:
        print("That's way too many")
    else:
        for i in range(student_num):
            get_info = student()
            students[i+1] = get_info
        while True:
                print(f"\n\033[91m=====STUDENT RECORDS=====\033[0m")
                for stud in students.keys():
                    print(f"Student {stud}. {students[stud]['Name']}")
                print(f"Enter 0 to --Exit--")
                choice = int(input("Which info you like to see? "))
                if choice == 0:
                    break
                else:
                    see_student_info(choice)
                quiz  = input("Do you want to take a quiz? ")
                counter = 1
                if quiz == "yes":
                    for i in students[choice]["Subjects"]:
                        print(f"{str(counter)}. {i}")
                        counter += 1
                    print(f"--Exit--")
                    subject_choice = input("Which Subject: ")
                    if subject_choice.lower() == "math" or subject_choice == "1":
                        print("You've chosen Math")
                        if students[choice]["Subjects"]["Math"] == "No Remarks Yet":
                            students[choice]["Subjects"]["Math"] = math_sub()
                        else:
                            print("You already have a grade")
                    elif subject_choice.lower() == "english" or subject_choice == "2":
                        print("You've chosen English")
                        if students[choice]["Subjects"]["English"] == "No Remarks Yet":
                            students[choice]["Subjects"]["English"] = english_sub()
                        else:
                            print("You already have a grade")
                    elif subject_choice.lower() == "filipino" or subject_choice == "3":
                        print("You've chosen Filipino")
                        if students[choice]["Subjects"]["Filipino"] == "No Remarks Yet":
                            students[choice]["Subjects"]["Filipino"] = filipino_sub()
                        else:
                            print("You already have a grade")
                    elif subject_choice.lower() == 'exit':
                        quit()
                else:
                    subject_view_choice = input("Do you want to see your subjects? ")
                    if subject_view_choice == "yes":
                        if subject_view(choice) == 'exit':
                            break
                        else:
                            continue
                
    exit_or_no = input("Do you want to exit? ")
    if exit_or_no == "yes":
        quit()
    elif exit_or_no.lower() == "no":
        continue
    else:
        print("Yes or no only")
        continue

        

            





