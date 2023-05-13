#April 29, 2023
#Arithmetic Calculator with user input between two numbers

def basic_op(operator, value1, value2):

        
        if operator == '+':
            sum = value1 + value2
            print(f"The sum of {value1} + {value2} is {sum}")
        elif operator == '-':
            diff = value1 - value2
            print(f"The difference of {value1} + {value2} is {diff}")
        elif operator == '*':
            prod = value1 * value2
            print(f"The product of {value1} + {value2} is {prod}")
        elif operator == '/':
            quo = value1 / value2
            print(f"The quotient of {value1} + {value2} is {quo}")
        else:
            print("Please Enter a Valid Operator(+, -, *, /)")

#another variation, remove the triple quotation marks(") to run
def var_basic_op(operator, value1, value2):
        
        if operator == '+':
            return print("The sum is", value1 + value2)
        elif operator == '-':
            return print("The difference is", value1 - value2)
        elif operator == '*':
            return print("The product is", value1 * value2)
        elif operator == '/':
            return print("The quotient is", value1 / value2)
        else:
            print("Please Enter a Valid Operator(+, -, *, /)")

    
def get_user():
    while True:
        choice = input("This is a simple calculator(press enter to continue, type 'exit' to quit) ")
        if choice == 'exit':
             quit()
        if choice == "":
            try:

                op = input("Enter Operator: ")
                num1 = int(input("Please Enter First Number: "))
                num2 = int(input("Please Enter Second Number: "))
                #choose between the two functions but they pretty much do the same, pick 1 and remove the forward slash(/).
                var_basic_op(op, num1, num2)
                
            except:
                print("Please Enter a Valid Number")
        else:
            print("\n\033[91m\033[1mPlease type as the instruction says\033[0m\n")
#Calling the function in order for it to execute
get_user()