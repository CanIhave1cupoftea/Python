#April 19, 2023
#Simple 4 operation calculator(+, - , *, /)

def calc(operator, value1, value2):
    if operator == '+':
        sum = value1 + value2
        print(f"You picked addition and the sum of the 2 numbers are {sum}")
        return sum
    elif operator == '-':
        diff = value1 - value2
        print(f"You picked subtraction and the difference of the 2 numbers are {diff}")
        return diff
    elif operator == '*':
        prod = value1 * value2
        print(f"You picked multiplication and the product of the 2 numbers are {prod}")
        return prod
    elif operator == '/':
        quo = value1 / value2
        print(f"You picked division and the quotient of 2 the numbers are {quo}")
        return quo
    else:
        print("Enter Valid Operator")
while True:
    ques = input("Gusto mo bang gumamit?? ")
    if ques == 'oo' or ques == 'OO':
        while True:
            try:
                op = input("Enter Operator to be Used: ")
                if op == 'ayoko na':
                    print("K")
                    break
                num1 = int(input("Enter First Number: "))
                num2 = int(input("Enter Second Number: "))  
                calc(op, num1, num2)
                    
            except:
                print("Enter Valid Number")
                continue
    else:
        print("K again")
        break           
    
    
