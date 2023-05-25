#May 23, 2023

#The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.What if the string is empty? Then the result should be empty object literal, {}.

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





