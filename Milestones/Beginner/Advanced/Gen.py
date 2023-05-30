#May 28, 2023
#Learning the generators
#Generators and iterators are the same, only, the generators exist inside a function. Basically, what generators do is they hold onto the value, much like an iterator, it will store the values once called using the next() method or a for loop to iterate over it
#The analogy I thought of is this, a generator is like a hand holding something without putting it into its pocket which is the computer memory.


"""import random

# fill in this function
def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b
        
    #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

print(type(range(1,11)))"""
"""
def luck():
    for i in range(7):

        yield random.randint(1,3)



import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)"""

#May 30, 2023
#Trying to learn what decorators are
#So a decorator is a function that modifies another function using a so called "wrapper function inside a function. :O"


"""def f1(func):
    def wrapper():
        print("Started")
        print(func())
        print("Ended")
    
    return wrapper()

def f2():
    return "Hey"

print(f1(f2))"""

#first the function will be sent as a parameter here
def uppercase(func):
    #then it will be re-evaluated, called and reprocessed here
    def wrapper(*args):
        return func(*args).upper()
    
    return wrapper


@uppercase
def uppcase_letters(word):
    return word

print(uppcase_letters("Hello"))
    