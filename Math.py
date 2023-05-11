#May 10, 2023
# Math subject
def odd_or_even(num):
    even = 0
    odd = 0
    for i in range(1, num+1):

        if i % 2 == 0:
            even += 1
        else:
            odd +=1

    return f"The Numbers of Even: {even} and Odd: {odd}" 
def prime_number(num):
    factors = 1
    if num > 1:
        for i in range(2, num+1):
            if num % i == 0:
                factors += 1

        return "It is not a prime number" if factors > 2 else "It is a prime number"
    else:
        return "Prime Numbers are greater than 1"

def factorial(num): 
    numbers = [i for i in range(num, 0, -1)]
    product = 1
    for i in numbers:
        product *= i
    return f"Factorial: {product:,}, {odd_or_even(num)} and {prime_number(num)}"

num = int(input("What is the number? "))
if 1 < num > 100:
    print("The number should not be less than 1 or greater than 100")
else:
    print(factorial(num))

    
    