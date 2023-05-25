#May 17, 2023

#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def prod_sum(num1, num2):
    #return the product if the product of 2 numbers are less than or equal to 1000, if not, return the sum instead
    return num1 * num2 if num1 * num2 <= 1000 else num1 + num2


def sum_of_c_p(n):
    #print the sum current number and previous number
    previous = 0
    for num in range(n):
        sum = previous + num
        previous = num
        print(previous, sum)
        
def print_even_index(s):
    #print only the letters at an even index/ print the even letters in a string

    for i in range(0,len(s),2):
        print(s[i])

def remove_character(s, n):
    #print a string with first letters removed, determined by n
    for i in range(n, len(s)):
        print(s[i], end="")

def first_last_same(l):
    #return True the first element of the list is the same as the last
    return l[0] == l[-1]

def div_by_5(x):
    #return only the list of numbers divisible by 5

    for n in x:
        if n % 5 == 0:
            print(n) 

def repeating(n):
    #print a right triangle by n times

    #1st solution
    for i in range(1, n):
        print(str(i) * i)
    
    #2nd solution
    for i in range(5):
        for j in range(i):
            print(i, end="")
        print()

def two_lists(l1, l2):
    #return a new list that contains the odd from the 1st list and even from the first list
    result = []
    for i, j in enumerate(l1):
        if j % 2 == 1:
            result.append(j)
        if l2[i] % 2 == 0:
            result.append(l2[i])

    return sorted(result)

#Write a Program to extract each digit from an integer in the reverse order
def reverse_num(n):
    n = 6478

    while n > 0:
        d = n % 10

        n //= 10
        print(d, end="")


    for i in str(n)[::-1]:
        print(i)


#Print multiplication table form 1 to 10
def multable():
    for n in range(1, 11):
        for i in range(1, 11):
            print(str(i * n).center(5), end=" ")
        print()

#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base, exp):
    return base ** exp


print(sum(range(10+1)))

import sys
print(sys.version)

