#May 20, 2023
#some exercises to solve


#In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants? More generally given parameters: p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass) the function nb_year should return n number of entire years needed to get a population greater or equal to p. aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

def nb_year(p0, percent, aug, p):
    # your code
    years = 0
    percent /= 100
    inhabitants = p0
    population = inhabitants * percent
    print(inhabitants)
    while inhabitants < p:
        inhabitants += (population + aug)
        population = inhabitants * percent
        years += 1
        
    return years


#Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

#example a = [121, 144, 19, 161, 19, 144, 19, 11]  b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

#my answer
def comp(array1, array2):
    # your code
    print(array2,"\n", array1)
    square_roots = [int(i**0.5) for i in array2]
    print(square_roots)
    return all([j in square_roots for j in array1] and [i in array1 for i in square_roots])

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 161*161, 19*19, 144*144, 19*19]

def two_sum(a, b):
    return 20 if 20 >= (a + b) >= 15 else a + b

#FizzBuzz: Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#fibonacci
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b
    
#Password Generator: Write a program that generates a random password of a given length. The password should contain a mix of uppercase letters, lowercase letters, numbers, and special characters.

import random
import string

def pass_gen(num):
    password = []
    for i in range(num):
        randoms = [random.choice(string.ascii_letters), random.choice(string.ascii_uppercase), random.choice(string.digits), random.choice(string.ascii_lowercase)]
        if i < len(randoms):
            password.append(randoms[i])
        else:
            password.append(random.choice(randoms))
    random.shuffle(password)
    return f"Password Generated: {''.join(password)}"


#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

#my answers
def duplic(text):
    duplicates = {}
    store = []
    for i in "indivisibility":
        if i not in store:
            store.append(i)
        elif i not in duplicates:
            duplicates[i] = 2
        elif i in duplicates:
            duplicates[i] += 1

    for i, j in duplicates.items():
        print(i, j)   

def duplicate_count(text):
    # Your code goes here
    if len(text) == 0: return 0
    storage = []
    duplicates = set()
    for i in text.lower():
        if i not in storage:
            storage.append(i)
        elif i not in duplicates:
            duplicates.add(i)
    return len(duplicates)

#best answer
def duplicate_count(s):
  new = set(s.lower())
  print(new)
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

print(duplicate_count("indivisibility"))