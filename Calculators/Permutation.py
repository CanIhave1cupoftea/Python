#May 27, 2023 3:15pm -
#Trying to figure out how to solve permutations and combinations
#Permutation is a way to arrange an element in different order - the order matters AB != BA
#Combination is also a way to arrange but the order does not matter, AB = BA
#Fomula of permutation: nPr = n!/n-r!
#Formula of combination: nCr = n!/(n-r)!*r! nPr/r!


some = ["A", "B", "C", "D"]

def fact(num):
    #this is for the arrangements of words
    total = 1
    if isinstance(num, list):
        for i in num:
            total *= fact(i)
        return total
    
    #this is for the arrangements inside a shelf, for example
    else:
        if num == 1 or num == 0:
            return 1
        else:
            return num * fact(num-1)

def permu(n, r):
    if isinstance(r, list):
        return fact(n)//fact(r)
    else:
        return fact(n)//fact(n-r)

def combi(n, r):
    return permu(n,r)//fact(r)

def count_repeat(word):
    return [value for value in {i: word.count(i) for i in word if word.count(i) > 1}.values()]
        
#In how many different ways can you arrange 3 books on a shelf from a group of 7

#print(combi(7,3))
#If checking the permutation ina word however, the n must be the length of the word and the r would be the repeating letters
#How many different ways can you arrange the letters in a word: ALABAMA

word = "math"
print(permu(8,3))



