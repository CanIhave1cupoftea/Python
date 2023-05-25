#May 20, 2023
#Some practice to understand the concept of lambda function
#A lambda function is a compact, usually one line of code that the programmers improve the readability of htier code to also lessen the time to do a formla function.

#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

add_15 = lambda num=0: num + 15
multiply = lambda num1, num2: num1 * num2

#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

def compute(n):
    return lambda x: x * n

#Write a Python program to sort a list of tuples using Lambda.

subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
grades = lambda grades: grades[1]
sorted_sub = sorted(subjects, key=grades)


#Write a Python program to sort a list of dictionaries using Lambda.
dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

make = lambda x: x["color"]
dict.sort(key=make)

#Write a Python program to filter a list of integers using Lambda.

orig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_odd = lambda x: x % 2 == 0

#Write a Python program to square and cube every number in a given list of integers using Lambda.

square = lambda x: x ** 2
cube = lambda x:x ** 3

#Write a Python program to find if a given string starts with a given character using Lambda.
istart = lambda x: x.startswith("j")

import functools
letters = ["J", "A", "C", "K", "S"]


my_set = set()
