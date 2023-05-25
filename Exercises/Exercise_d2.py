#May 18, 2023

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year)

def ageIn100Years(n, a, y):
    age = (100 - a) + y
    return f"Your name is {n} and you are {a} years old, the year is {y}, you will turn 100 years old in year {age}"

def add_binary(a,b):
    """Adds a and b together and returns a binary string"""
    return bin(a + b)[2::]

print(add_binary(5, 9))

