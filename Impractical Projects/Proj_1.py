#May 26, 2023 5:54pm
#Project 1: Silly Name Generator

#In this warm­up project, you’ll write a simple Python program that generates nutty
#names by randomly combining first names and surnames. With any luck, you’ll produce
#a plethora of aliases that would make any sidekick proud. You’ll also review bestpractice coding guidelines and apply external programs that will help you write code
#that conforms to those guidelines

from random import choice


first = ('John', 'Doraemon', 'Shinigami', 'Makibao')
last = ('Shrek', 'Tom', 'Dagul', 'Heisenberg')

#print(f"{choice(first)} {choice(last)}")


#Additional Practices with strings
#To form Pig Latin, you take an English word that begins with a consonant, move that consonant to the end, and then add “ay” to the end of the word. If the word begins with a vowel, you simply add “way” to the end of the word.
#Pig Latin rephraser

def pig_latin(word):
    return f"{word[1:]}way" if word[0].lower() in 'aeiou' else f"{word[1:]+word[0]}ay"

#print(pig_latin("Anix")) 


