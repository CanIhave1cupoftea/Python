"""class Student:


    def GetStudent(self):
        self.__rollno = input("Enter Roll No:")
        self.__name = input("Enter Name:")
        self.__physicsMarks = int(input("Enter Physics Marks:"))
        self.__chemistyMarks = int(input("Enter Chemistry Marks:"))
        self.__mathMarks = int(input("Enter Maths Marks:"))
        return(self.__rollno)

    def PutStudent(self):
        print(self.__rollno,self.__name,((self.__physicsMarks+self.__chemistyMarks+self.__mathMarks)/3))
    def Search(self,min,max):
        per = (self.__physicsMarks+self.__mathMarks+self.__chemistyMarks)/3
        if(per>=min and per<=max):
            return True
        else:
            return False

# creating a dictionary to store student record 
studentDict = dict()
n = int(input("How Many Students you Want To Input?"))
for i in range(n):
 S = Student()
 rollno = S.GetStudent()
 studentDict.setdefault(rollno,S)

# Searching for student records with roll numbers provided by the user.
rollno = input("Enter Roll Number you Want Search?")
S = studentDict.get(rollno,"Not Found!")
if(isinstance(S,Student)):
    S.PutStudent()
else:
    print(S)

# Printing records of all users with marks greater than 60% 
print("All students who scored more that 60 percentage are : ")
gradeAStudent = list(filter(lambda s:s.Search(60,100),studentDict.values()))
if(len(gradeAStudent) == 0):
    print("Record Not Found!")
else:
    for S in gradeAStudent:
        S.PutStudent()"""

#string methods




"""
print("ECHO CHAMBER".center(30, "="))
user = input("Enter something: ")
print("GENERATING", end="")

timer = 0
for i in range(12):
    timer += 1
    typethis(".")
    if timer > 3:
        timer = 0
        print("\b\b\b", end="")"""
    
"""
typethis(mod.bold(mod.purple("ARNEL THE GREAT! 20/73")))"""

#code wars May 15, 2023
"""
def rental_car_cost(d):
  return (d > 3) + 20
  return d * 40 - 1 * 20 - (d > 6) * 30

print(rental_car_cost(2))
2 * 40 - 20"""

"""def DNA_strand(dna):
    # code here
    replaced = []
    for i in dna:
        if i == "A":
            replaced.append(i.replace("A", "T"))

        elif i == "T":
            replaced.append(i.replace("T", "A"))
        elif i == "G":
            replaced.append(i.replace("G", "C"))
        elif i == "C":
            replaced.append(i.replace("C", "G"))
    return "".join(replaced)
    #Best solution
    return dna.translate(str.maketrans("ATCG","TAGC"))
print(DNA_strand("TTAA"))"""


"""def validate_pin(pin):
    
    #return true or false
   
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()

def factorial(num):
    arr = []
    for number in range (1, num+1):
        arr.append(number)
    print(arr)
    return expo

print(factorial(5))"""

"""def is_isogram(string):
    #your code here
    checker = []
    for i in string:
        if i.lower() not in checker:
            checker.append(i.lower())
    print(checker)
    print("".join(checker))
    return "".join(checker) == string.lower()
    
   
    
print(is_isogram("moOse"))"""

"""def disemvowel(string_):
   

    return string_.translate(string_.maketrans({"a": "", "e": "", "i": "", "o": "", "u": "", "A": "", "E": "", "I": "", "O": "", "U": ""}))

print(disemvowel("GoOd night Sam!"))
    """

""" def square_digits(num):
    # Your code here
    conv = str(num)
    conc = []
    for i in conv:
        
        
        conc.append(str(int(i) ** 2))
    return int("".join(conc))

print(square_digits(9119))"""

"""def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    sum_of_pos = []
    sum_of_neg = []
    
    for i in arr:
        if i > 0:
            sum_of_pos.append(i)
        elif i < 0:
            sum_of_neg.append(i)
       
    
    
    return [len(sum_of_pos), sum(sum_of_neg)]

print(count_positives_sum_negatives([]))"""

"""def reverseseq(n):
    return range(n, 0, -1)

print(reverseseq(10))"""
"""def see(arr):
    x = [int(i[:1]) for i in arr]
    y = [int(i[2:]) for i in arr]
    score = 0
    access = 0
    for num in x:
        if num > y[access]:
            score += 3
        elif num == y[access]:
            score += 1
        access += 1
    return score
    


print(see(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))"""


"""def printer_error(s):
    # your code
    error = [i for i in s.lower() if i not in 'abcdefghijklmn']
    return f"{len(error)}/{len(s)}"

print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))"""

#You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

"""#my answer
def get_middle(s):
    measure = len(s) // 2
    if len(s) % 2 == 0:
        return f"{s[measure-1:measure+1]}"
    else:
        return f"{s[measure:measure+1]}"
#answers i like
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s
print(get_middle("sevens"))

def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]"""

#Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

"""def double_char(s):
    return "".join([i * 2 for i in s])



print(double_char("hello"))"""

#If you can't sleep, just count sheep!! Task: Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

#my answer
"""def count_sheep(n):
    # your code
    if n >= 0:
        return "".join([str(i) + " sheep..." for i in range(1, n) ])
    
#my fave answer
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))"""

#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.It should remove all values from list a, which are present in list b keeping their order.

#cant figure it out for now
"""
def array_diff(a, b):
    #your code here
    if not b: return a

    if 
    a = set(a)
    for i in a:
        
        if i in b:
            a.remove(i)
        
    return a

print(array_diff([1,2,2], [2]))"""

"""#Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.

#my answer

def minimum(arr):
    #your code here...
    smallest = None
    for num in arr:
        if smallest == None:
            smallest = num
        elif num < smallest:
            smallest = num
    return smallest
def maximum(arr):
    #...and here
    biggest = None
    for num in arr:
        if biggest == None:
            biggest = num
        elif num > biggest:
            biggest = num
    return biggest
"""

#A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

#A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""
#my answer
def is_pangram(s):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if s.lower().count(i) < 1:
           return False
    return True
 
#my fave answer
import string
def is_pangram(s):
    return all([c in s.lower() for c in string.ascii_lowercase])

print(is_pangram('The quick, brown fox jumps over the lazy dog!'))"""

'''def find_smallest_int(arr):
    # Code here
    smallest = None
    for num in arr:
        if smallest == None:
            smallest = num
        elif num < smallest:
            smallest = num
        return smallest
    
print(find_smallest_int([78, 56, 232, 12, 11, 43]))
'''
#Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

"""#my answer
def persistence(n):
    # your code
    persistence = 0
    while n > 9:
        x = []
        mul = 1
        for i in str(n):
            print(i)
            x.append(i)
        print(x)
        for num in x:
            mul *= int(num)
        n = mul
        persistence += 1
    return persistence
#shortest answer
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i"""

#There is an array with some numbers. All numbers are equal except for one. Try to find it! find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
#find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55


""""def find_uniq(arr):
    # your code here
    for i in arr:
        if arr.count(i) == 1:
            return i

print(find_uniq([  0, 0, 0.55, 0, 0 ]))"""

#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.Examples:Input: 42145 Output: 54421Input: 145263 Output: 654321Input: 123456789 Output: 987654321
"""#my answer
def descending_order(num):
    # Bust a move right here
    if num > 0:
        j = []
        for i in str(num):
            j.append(i)
        return int("".join(sorted(j,reverse = True)))
    
    return 0

#best answer
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
  """  """

def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) == 10:
        d = None
        equal = False
        for i in walk:
            if d == None:
                d = i
            elif d == 'w':
                if walk.count(d) - walk.count('e') == 0:
                    equal = True
                d = i
            elif d == 'e':
                if walk.count(d) - walk.count('w') == 0:
                    equal = True
                d = i
            elif d == 'n':
                if walk.count(d) - walk.count('s') == 0:
                    equal = True
                
                d = i
            elif d == 's':
                if walk.count(d) - walk.count('n') == 0:
                    equal = True
                
                d = i
            else:
                equal = False
        return equal

"""

"""print(is_valid_walk(['w', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 'e']))
    """

#Given an array of integers, find the one that appears an odd number of times.
"""
There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd)."""
"""
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0] #this selects the index of the filtered element which is in this case, x"""

#Create a function with two arguments that will return an array of the first n multiples of x.

#Assume both the given number and the number of times to count will be positive numbers greater than 0.Return the results as an array or list( depending on language ).Examplescount_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]count_by(2,5) #should return [2,4,6,8,10]

#ai answer  
"""def count_by(x, n):
    
    Return a sequence of numbers counting by `x` `n` times.
    
    current = x
    list = []
    
    for i in range(n):
        
        if current > 0:

            list.append(current)
            current += x
           
        else:
            break
    
    return list
"""
#shortest answer
"""def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

"""

#Make a function that will output the square numbers
print([i*i for i in range(1,11)])