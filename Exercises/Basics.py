#May 18, 2023
#Compiling the basics of python I've known so far...

#First we have different data types

"""We have primitive data types which are:
int (integers) whole numbers from below 0 and above 0
float (fractions) numbers that are fractions
strings (words/letters/characters) anything the comprises a letter or a word

We also have sequential data types which are:
lists, lists are ordered(they have index), mutable(changeable), allows duplicates
tuples, tuples are ordered but not mutable, also allows duplicates
set, set does not allow duplicates and is unoreded but mutable

"""

#Strings

"""
We have strings that are iterable, behaves like an array, an array of letters. We can perform operations on them typically and only multiplication and addition(concatenation)

We can access the contents or letters of string using string indexing which is enclosed by a pair of square brackets, the number we put inside is the number of the index of the letter we are trying to access, or whatever the number is (starting from 0, negative numbers start from the end) will return the letter from that position

We can also do string slicing which is like string indexing but this time it has colons, the syntax is [start:end:step]
the start is inclusive, it will include the letter from that index but the end is exclusive, it will exclude the letter from the index given, the step is the interval in between those indices


"""

#Assignment operators
"""
'=' equal sign is used to assign a value to a variable
'+= used to add something from the right and then assign that value on the variable, this will work with other operations such as minus, multiplication, division, floor division

':=' walrus operator is used to give a value to a variable while simultaneously being part of an expression

"""

 #Arithmetic operations
"""
 exponent '**'
 multiplication '*'
 division '/'
 floor division '//' return the integer
 i will go back here when i got full understanding


"""
#variables, should not start with a number, cannot contain any special characters or  space but can contain underscore
#we can assignment multiple variables and value in a single line

a, b, c = 1, 2, 3
#if we print this the output would be 1 2 3

#we can also write multiple statements on a single line using semi-colon

l = 2; c = 2

#a statement is an instruction that python can execute
# we have 4 different statements, print, assignment, if, looping statements
