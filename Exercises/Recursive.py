#May 22, 2023
#Recursion

#fibonacci
#recursive function

def fac(n) -> int:
    if n == 1:
        return 1
    else:
        print("process")
        return n * fac(n-1) 



def is_Power_of_two(n):
        return n > 0 & (n and (n - 1)) == 0
print(is_Power_of_two(5))

#Write a Python program to check if a given positive integer is a power of three.

def ispower(n):
    while n % 3 == 0:
        n /= 3
    return n == 1

print(ispower(97))