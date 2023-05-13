#April 20, 2023
#Pythagorean Theorem is the relationship between the sides of right triangle and its formula " a² + b² = c², a and b are the lengths of triangle and c is the hypotenuse
# A and B are the other legs of a triangle, C is always the hypotenuse.Given that, the value of A and B are reversible and can be swapped and you will still arrive at the same answer

import math

def hypotenuse(a, b):

    try: 
        a = int(a)
        b = int(b)
        print(f"\033[91m {a}² + {b}² = c² \033[0m")
        side_c = pow(a, 2) + pow(b, 2)
        hypotenuse = math.sqrt(side_c)

        if hypotenuse.is_integer():
            print(f"\033[0m\033[92mThe Length of the Hypotenuse is {abs(round(hypotenuse))}\033[0m")
        else:
            print(f"\033[92mThe Length of the Hypotenuse is √{abs(side_c)} ≈ {round(hypotenuse, 2)}\033[0m")

    except:
        print("\033[91mInvalid Input, Please Recheck\033[0m")
        print("\033[1mNOTE:\033[0m You can always type 'exit' at any of the sides to close the program anytime\n")

    else:
        print("\033[36m\033[1m========================================\033[0m\n")

def side_a(b, c):
    try:
        b = int(b)
        c = int(c)
        print(f"\033[91ma² + {b}² = {c}²\033[0m")
        a = pow(c, 2) - pow(b, 2)
        side_a = math.sqrt(a)
        
        if side_a.is_integer():
            print(f"\033[92mThe Length of the Side A is {abs(round(side_a))}\033[0m")
        else:
            print(f"\033[92mThe Length of the Side A is √{abs(a)} ≈ {round(side_a, 2)}\033[0m")
    except:
        print("\033[91mInvalid Input, Please Recheck")
        print("\033[1mNOTE:\033[0m You can always type 'exit' at any of the sides to close the program anytime\n")

    else:
        print("\033[36m\033[1m========================================\033[0m\n")

def side_b(a, c):
    try:
        side_a = int(a)
        side_c = int(c)
        print(f"\033[91m{a}² + b² = {c}²\033[0m")
        b = pow(side_c, 2) - pow(side_a, 2)
        side_b = math.sqrt(b)

        if side_b.is_integer():
            print(f"\033[92mThe Length of the Side B is {abs(round(side_b))}\033[0m")
        else:
            print(f"\033[92mThe Length of the Side B is √{abs(b)} ≈ {round(side_b, 2)}\033[0m")
    except:
        print("\033[91mInvalid Input, Please Recheck\033[0m")
        print("\033[1mNOTE:\033[0m You can always type 'exit' at any of the sides to close the program anytime\n")

    else:
        print("\033[36m\033[1m========================================\033[0m\n")


def ask(a_side, b_side, c_side):



    if (a == '?' and c == '?') or (b == '?' and c == '?') or (a == '?' and b == '?'):
        print("\033[91mOne Blank(?) Side Only\033[0m")

    elif a == '?':
        side_a(b=b_side, c=c_side)        

    elif b == '?':
        side_b(a=a_side, c=c_side)
    
    elif c == '?':
        hypotenuse(a=a_side, b=b_side)

    else:
        print("\033[91mPlease Enter At Most 2 Numbers and a Question Mark\033[0m")
        print("\033[1mNOTE:\033[0m You can always type 'exit' at any of the side to close the program anytime\n" )

while True:
    print("""\033[1m\033[36m=====PYTHAGOREAN THEOREM CALCULATOR=====\033[0m
Type 'exit' if you wanna exit the program
\033[1mPlease type '?' as a value for the missing side\033[0m\n""")
    

    a = input("\033[93mPlease Enter Side A: ")
    if a == 'exit':
        print("\033[92m\033[1mTHANK YOU FOR USING PYTHAGOREAN CALCULATOR!!!\033[0m")
        break

    b = input("Please Enter Side B: ")
    if b == 'exit':
        print("\033[92m\033[1mTHANK YOU FOR USING PYTHAGOREAN CALCULATOR!!!\033[0m")
        break

    c = input("Please Enter Side C: ")
    if c == 'exit':
        print("\033[92m\033[1mTHANK YOU FOR USING PYTHAGOREAN CALCULATOR!!!\033[0m")
        break
    
    ask(a, b, c)
