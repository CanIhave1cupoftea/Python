#Mathematical opoerator with user input
"""def basic_op(operator, value1, value2):
    

        if operator == '+':
            print(f"{operator}, {value1}, {value2},", first_val + second_val)
        elif operator == '-':
            print(f"{operator}, {value1}, {value2},", first_val - second_val)
        elif operator == '*':
            print(f"{operator}, {value1}, {value2},", first_val * second_val)
        elif operator == '/':
            print(f"{operator}, {value1}, {value2},", first_val / second_val)
        else:
            print("Please Enter a Valid Operator(+, -, *, /)")

    
try:
        op = input("Enter Operator: ")
        val1 = input("Please Enter First Number: ")
        val2 = input("Please Enter Second Number: ")
        first_val = int(val1)
        second_val = int(val2)
        basic_op(op, val1, val2)
except:
        print("Please Enter a Valid Number")
        
def basic_op(operator, value1, value2):
        
        if operator is '+':
            sum = value1 + value2
            print(f"('{operator}', {value1}, {value2}) --> {sum}") 
            return sum
        elif operator == '-':
            difference = value1 - value2
            print(f"('{operator}', {value1}, {value2}) --> {difference}")
            return difference
        elif operator == '*':
            product = value1 * value2
            print(f"('{operator}', {value1}, {value2}) --> {product}")
            return product
        elif operator == '/':
            quotient = value1 / value2
            print(f"('{operator}', {value1}, {value2}) --> ", value1 / value2)
            return quotient
        
basic_op('*', 12, 12)"""

def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8
print(simple_multiplication(9))

