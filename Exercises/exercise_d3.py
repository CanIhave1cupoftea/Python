#May 19, 2023
#You might know some pretty large perfect squares. But what about the NEXT one? Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer. If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

#My answer
def find_next_square(sq):
    
    square_root = int(sq ** .5)
    print(square_root)
    if sq ** .5 == square_root:
        square_root += 1
        return square_root ** 2
    else:
        return -1


#intriguing answer

def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2

#Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

#my answer
def invert(lst):
    inverse = lambda x:x * -1
    return list(map(inverse, lst))
#best answer
def invert(lst):
    return [-x for x in lst]


#A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive? Return true if yes, false otherwise :)

#my answer
def hero(bullets, dragons):
    return bullets >= dragons * 2

#The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc. Given a year, return the century it is in.

#my answer
def century(year):
    # Finish this :)
   
    return    year // 100 + 1 if year / 100 % 1 else year // 100

#best answer
def century(year):
    return (year + 99) // 100

#Complete the solution so that the function will break up camel casing, using a space between words. "camelCasing"  =>  "camel Casing"
#"identifier"   =>  "identifier" ""             =>  ""

def solution(s):
    break_up = []
    for i in s:
        if i in s.lower():
            break_up.append(i)
        else:
            break_up.append(" ")
            break_up.append(i)
    return "".join(break_up)
#best answer
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

#In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it. "a" = 1, "b" = 2, etc

#my answer
import string
def alphabet_position(text):
    for i in text:
        if i.isdigit():
            return ""
    
    string_to_alp = text.maketrans({"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", "i": "9", "j": "10", "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", "p": "16", "q": "17", "r": "18", "s": "19", "t": "20", "u": "21", "v": "22", "w": "23", "x": "24", "y": "25", "z": "26", "'": "", ".": ""})
    new_string = text.replace(" ", "")
    
    strin = []
    for i in new_string.lower():
        if i not in string.punctuation:
            strin.append(i)
    

    
    final = " ".join(strin)
    
    return final.translate(string_to_alp)

#best answer
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())



#other answers
def alphabet_position(text):
    
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    l = [] 
    
    for i in text:
        if i in upper_alpha:
            index = upper_alpha.index(i) + 1
            l.append(str(index))
        elif i in lower_alpha:
            index = lower_alpha.index(i) + 1
            l.append(str(index)) 
    return " " .join(l)

#import string so we can generate the alphabets using string.ascii
import string

def alphabet_position(text):
    lower_case_text = text.lower() #convert the given text into all lowercase letters
    alphabet = string.ascii_lowercase # generate lowercase letters from the string module
    number = list(range(1, 27)) #generate numbers from 1-26
    dict_alphabet_number = dict(zip(alphabet, number)) # combine the aphabets in a dictionary using dict and zip
    collector = [] # create a container to old the numbers generated from the loop
    
    for element in lower_case_text: 
        if element in alphabet:
            collector.append(str(dict_alphabet_number[element])) 
    return ' '.join(collector)
    

#Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest. Write a function that returns both the minimum and maximum number of the given list/array.[1,2,3,4,5] --> [1,5] [2334454,5] --> [5,2334454] [1]         --> [1,1]

#my answer
def min_max(lst):
    smallest = None
    biggest = None
    value = []
    for i in lst:
        if smallest == None:
            smallest = i
        if biggest == None:
            biggest = i
        elif i < smallest:
            smallest = i
        elif i > biggest:
            biggest = i
    value.append(smallest)
    value.append(biggest)
    
    return sorted(list(value))

#to study
def min_max(lst):
  # Too easy, but requires two pases
  # return[min(lst), max(lst)]
  
  # Single pass:
  l, u = None, None
  for n in lst:
      if l is None or n < l:
          l = n
      if u is None or n > u:
          u = n
  return [l, u]

#Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character. For example, a tower with 3 floors looks like this:

#my answer
def tower_builder(n_floors):
    tower = []
    increment = 1
    floor = n_floors 
    for i in range(n_floors):
        floor -= 1
        tower.append(" "*floor + "*" * increment + " " *floor)
        increment += 2
    return tower

#best answer
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


print("Hello World!?.'".translate( [i  for i in 'abcdefghijklmnopqrstuvwxyz']))
