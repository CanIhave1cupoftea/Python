#May 12, 2023 9:00am - 7:53pm
#Simple quiz game with score
"""I want to create a quiz that will have 3 categories with 5 questions each and save the score to their respective category and also be able to have the total score from these"""

import time

python_score = "No Score Yet"
html_score = "No Score Yet"
css_score = "No Score Yet"
total_score = "No Total Yet"
categories = {"Python":python_score, "HTML": html_score, "CSS": css_score, "TOTAL": total_score}

def python_scoring():
    global python_score
    python_score = 0

    print("python quiz".upper().center(30, "•"))
    questions = {
        "What is the primitive data type that is a number that has decimal point?",
        "What is the primitive data type that contains characters or words?",
        "What will be the output of this code: print(5 > 2) ?",
        "What function can you use to know the data type of an object?",
        "What function should you use if you want to output something?"
    }
    python_answers = (
                    'string',
                    'print',
                    'float',
                    'True', 
                    'type', 
                    'str', 
                    'type()', 
                    'print()'  
    )
    
    for question in range(len(questions)):
        print(f"{question+1}. {questions.pop()}")
        answer = input("Answer: ")
        if answer in python_answers:
            python_score += 1

    print(f"You scored {python_score}")
    return "You did well!☻☻☻" if python_score > 4 else "Nice Try!☻"

def python_category():
    print("Category Selected: PYTHON")
    while True:
        try:   
            if python_score == "No Score Yet":
                while True:
                    choice = input("You have no score yet, do you want to take the quiz? ")
                    if choice.lower() == "yes":
                        print(python_scoring())
                        break
                    elif choice.lower() == "no":
                        raise Exception
                    else:
                        print("'Yes' or 'No' only")
                        continue
            elif python_score >= 0:
                print()
                print(f"Your last score is {python_score}/5")
                while True:
                    choice = input("Would you like a retake? ")
                    if choice.lower() == "yes":
                        print(python_scoring())
                        break
                    elif choice.lower() == "no":
                        raise Exception
                    else:
                        print("'Yes' or 'No' only")
                        continue
        except Exception:
            print("GOING BACK TO MAIN MENU", end=" ")
            for load in range(3):
                time.sleep(0.5)
                print("► ", end="")
            break
def html_category():
    print("Category Selected: HTML")
    while True:
        try:
            if html_score == "No Score Yet":
                while True:
                    choice = input("You have no score yet, do you want to take the quiz? ")
                    if choice.lower() == "yes":
                        print(html_scoring())
                        break
                    elif choice.lower() == "no":
                        raise Exception
                    else:
                        print("'Yes' or 'No' only")
                        continue
                
            elif html_score >= 0:
                print()
                print(f"Your last score is {html_score}/5")
                while True:
                    choice = input("Would you like a retake? ")
                    if choice.lower() == "yes":
                        print(html_scoring())
                        break
                    elif choice.lower() == "no":
                        raise Exception
                    else:
                        print("'Yes' or 'No' only")
                        continue
        except Exception:
            print("GOING BACK TO MAIN MENU", end=" ")
            for load in range(3):
                time.sleep(0.5)
                print("► ", end="")
            break
def html_scoring():
    global html_score
    html_score = 0
    print("html quiz".upper().center(30, "•"))

    questions = {
        "Does <br> need a closing tag?",
        "In which html tag should you input the <meta> tag?",
        "What is the tag that makes an element clickable?",
        "What is the list that contains bullet?",
        "What attribute should be inside the link tag to link the document onto that location?"
    }
    html_answers = (
                    'no',
                    'head',
                    '<head></head>',
                    '<head>', 
                    'button', 
                    '<button>', 
                    'ul', 
                    'unordered list',
                    'href'
    )
    
    for question in range(len(questions)):
        print(f"{question+1}. {questions.pop()}")
        answer = input("Answer: ")
        if answer in html_answers:
            html_score += 1

    print(f"You scored {html_score}")
    return "You did well!☻☻☻" if html_score > 4 else "Nice Try!☻"

def css_category():
    print("Category Selected: CSS")
    while True:
        try:
            if css_score == "No Score Yet":
                while True:
                    choice = input("You have no score yet, do you want to take the quiz? ")
                    if choice.lower() == "yes":
                        print(css_scoring())
                        break
                    elif choice.lower() == "no":
                        raise Exception
                    else:
                        print("'Yes' or 'No' only")
                        continue
                
            elif css_score >= 0:
                print()
                print(f"Your last score is {css_score}/5")
                while True:
                    choice = input("Would you like a retake? ")
                    if choice.lower() == "yes":
                        print(css_scoring())
                        break
                    elif choice.lower() == "no":
                        raise Exception
                    else:
                        print("'Yes' or 'No' only")
                        continue
        except Exception:
            print("GOING BACK TO MAIN MENU", end=" ")
            for load in range(2):
                time.sleep(0.5)
                print("► ", end="")
            break

def css_scoring():
    global css_score
    css_score = 0
    print("css quiz".upper().center(30, "•"))

    questions = {
        "What css property specifies the color of the background?",
        "What creates space around an element and is outside border?",
        "Multi-line comments are enclosed by?",
        "Is this the correct way to write css: color:#fff {h1} ?",
        "This makes the element fixed to it's place, even if the page is scrolled"
    }
    css_answers = (
                    'fixed',
                    'no',
                    'margin',
                    'background-color', 
                    '/**/', 
                    '/* */',
                    'fixed position',
                    'background-color:'
    )
    
    for question in range(len(questions)):
        print(f"{question+1}. {questions.pop()}")
        answer = input("Answer: ")
        if answer in css_answers:
            css_score += 1

    print(f"You scored {css_score}")
    return "You did well!☻☻☻" if css_score > 4 else "Nice Try!☻"

def main():
    
    while True:
        count = 1
        print()
        print("QUIZ GAME".center(30, "="))        
        print("Categories".center(30, "-"))
        for categ in categories.keys():
            print(f"{count:>10}. {categ}")
            count += 1
        print(f"{count:>10}. Exit")
        print(f"".center(30, "-"))
        view = input("Select Category: ")
        print()
        if view.lower() == "python" or view == "1":
            python_category()
        elif view.lower() == "html" or view == "2":
            html_category()
        elif view.lower() == "css" or view == "3":
            css_category()
        elif view.lower() == "total" or view == "4":
            print(total())
        elif view.lower() == "exit" or view == "5":          
            for letter in "THANK YOU FOR PLAYING THE GAME!":
                time.sleep(0.09)
                print(letter, end="")
            print("☻")
            quit()
        else:
            print("Select only from the categories")
            continue

def total():
    print("SCORES".center(30, "↔"))
    global total_score
    global categories
    if type(python_score) == int == type(html_score) and type(css_score) == int:
        total_score = 0
        total_score = python_score + html_score + css_score
        categories = {"Python":python_score, "HTML": html_score, "CSS": css_score, "TOTAL": total_score}
        for categ, score in categories.items():                 
            if type(score) == int:
                if categ != "TOTAL":
                    print(f"{categ:-<10} {score}/5")
                else:
                    print(f"".center(30, "↔"))
                    print(f"{categ:-<10} {score}/15\n")
            else:
                print(f"{categ:-<10} {score}")

        print(f"You got {total_score} questions right!")
        return "OUTSTANDING PERFORMANCE!" if total_score >= 12 else "BRAVO!"
        
    else:
        categories = {"Python":python_score, "HTML": html_score, "CSS": css_score, "TOTAL": total_score}
        for categ, score in categories.items():
            if type(score) == int:
                if categ != "TOTAL":
                    print(f"{categ:-<10} {score}/5")
            else:              
                print(f"{categ:-<10} {score}")
        return "Finish all the categories to see your total score"
    
main()
