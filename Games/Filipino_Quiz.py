#May 10, 2023
#Simple English -Filipino Translator
import random

english_words = ["brave", "sharp", "dog", "banana", "king", "show", "stone"]
filipino_answers = ["matapang", "matulis", "aso", "saging", "hari", "ipakita", "bato"]

def filipino_sub():
    score = 0
    for word in range(5):
        english_word = english_words.pop(random.randint(0, len(english_words)-1))
        print(f"Translate this word- {english_word} -")
        answer = input("Enter your answer: ")
        if answer.lower() in filipino_answers:
            score += 20

    return score


def filipino_remark():
    if filipino_sub() < 80:
        return "Failed"
    else:
        return "Passed" 

print(filipino_remark())