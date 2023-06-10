#May 23, 2023

#The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.What if the string is empty? Then the result should be empty object literal, {}.
"""
def count1(s):
    # The function code should be here
    if s == 0: return {}
    string = {}
    for i in s:
        if i not in string:
            string[i] = 1
        else:
            string[i] += 1

    
    return string

    
#best answer
def count(string):
  
    return {i: string.count(i) for i in string}

from collections import Counter
string = "abacadabada"
counted = Counter(string)




from collections import deque

a = deque()
a.append("shawarma")


from collections import namedtuple

b = namedtuple('b', 'x,y')
c = b(1, 2)
print(0o123)


#6 kyu exercise, return the highest scoring string
from string import ascii_lowercase

def high(x):
    # Code here
    value = {i: str(ord(i)-96) for i in ascii_lowercase}
    translated = [sum([int(letters.translate(str.maketrans(value))) for letters in words]) for words in x.split()]
    return x.split()[translated.index(max(translated))]

print(high('what time are we climbing up the volcano'))

#best answer
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
"""
#The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    #your code hereda
    return ''.join(["(" if word.count(i) == 1 else ")" for i in word.lower()])
    
print(duplicate_encode("recede"))