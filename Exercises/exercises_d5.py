#May 21, 2023

#Given an array of ones and zeroes, convert the equivalent binary value to an integer. Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

#my answer
def binary_array_to_number(arr):
  # your code
    arr.reverse()
    binary = []
    for i, j in enumerate(arr):
        if j == 1:
            binary.append(j * 2**i)
    
    return (sum(binary))


#clever answer
def binary_array_to_number(arr):
    return int(''.join(str(a) for a in arr), 2)


#In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 

def wave(people):
    # Code here
    wave = []
    for i, j in enumerate(people):
        if j.islower():
            new_string = people[:i] + j.upper() + people[i+1:]
            print
            wave.append(new_string)
    return wave
#shortest answer
def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]


#Your function takes two arguments: current father's age (years current age of his son (years Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future

"""def twice_as_old(dad_years_old, son_years_old):
    years = 0
    dad = dad_years_old
    son = son_years_old

    if dad < son * 2:
        while dad != son * 2:
            dad -= 1
            son -= 1
            years += 1
    else:
        while dad != son * 2:
            dad += 1
            son += 1
            years += 1
    return years"""

#best answer
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2*son_years_old)

#The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared). Eighty one (81), is the first number in having this property (not considering numbers of one digit). The next one, is 512. Let's see both cases with the details

def power_sumDigTerm(n):
    #your code here
    # n-th term of the sequence, each term is a power of the sum of its digits
    added = []
    
    for i in str(n):
        added.append(int(i))
    
    nth = 1
    total = sum(added)
    while n != total:
        n /= total
        nth += 1
     
    print(total ** nth)
    print(total)
    print(nth)

#Write a program that takes a list of tuples as input and sorts the list based on a specific element within each tuple.

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95), ("Eve", 88)]

print(scores[1])
score = lambda scores:scores[1]
sorted_scores = sorted(scores, key=score)
print(sorted_scores)