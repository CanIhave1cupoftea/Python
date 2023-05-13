#May 5, 2023 
#Solving Quadratic Equation using the Quadratic Formula
#Quadratic Equation: ax² + bx + c = 0
#Quadratic Formula: x = (-b ± sqrt(b² - 4ac)) / 2a; disriminant formula: (b² - 4ac)
#This Quadratic Equation does not include check the quadratic but will definitely be working on that in the future

import cmath as cm
import math as m
from fractions import Fraction as f

def discriminant(a, b, c):
    return (b**2)-(4*a*c)

def quadratic_formula(a, b, c):
    if discriminant(a, b, c) >= 1:
        sol1 = ((-1 * b) + m.sqrt(discriminant(a, b, c)))/(2*a)
        sol2 = ((-1 * b) - m.sqrt(discriminant(a, b, c)))/(2*a)
        print("The discriminant is positive! Therefore are 2 real solutions, these are x = {0:.0f} and x = {1:.0f}".format(sol1, sol2))
    
    elif discriminant(a, b, c) == 0:
        sol1 = (-b)
        sol2 = (2*a)
        print("The discriminant is zero! Therefore is only 1 solution, x = {0}".format(f(sol1, sol2)))
    else:
        sol1 = ((-1 * b) + cm.sqrt(discriminant(a, b, c)))/(2*a)
        sol2 = ((-1 * b) - cm.sqrt(discriminant(a, b, c)))/(2*a)
        print("The discriminant is negative! Therefore are 2 complex solutions, x = {0:.0f} and x = {1:.0f}".format(sol1,sol2))

#User input about the value of quadrattic equation
while True:
        choice = input("\033[96mSolve Quadratic Equations or Leave? \033[0m]")
        if choice == "leave":
            quit()
        elif choice == "exit":
            quit()
        elif choice == "no":
            quit()
        elif choice == "yes" or choice == "solve":
            try:

                a = int(input("Please Enter the value of a: "))
                b = int(input("Please Enter the value of b: "))
                c = int(input("Please Enter the value of c: "))

                if a == 0:
                    print("\033[91mThe value of 'a' can't be 0\033[0m")
                elif b == 0:
                    print(f"{a}x²{c} = 0")
                elif c == 0:
                    print(f"{a}x²+{b}x = 0")
                elif b < 0: 
                    if b < 0 and c < 0:
                        print(f"{a}x²{b}x{c} = 0")
                    else:
                        print(f"{a}x²{b}x+{c} = 0")
                elif c < 0:
                    if b < 0 and c < 0:
                        print(f"{a}x²{b}x{c} = 0")
                    else:
                        print(f"{a}x²+{b}x{c} = 0")
                elif b < 0 and c < 0:
                    print(f"{a}x²{b}x{c} = 0")
                elif a == 1:
                    if a == 1 and b == 1:
                        print(f"x²+x+{c} = 0")
                    else:
                        print(f"x²+{b}x+{c} = 0")

                elif b == 1:
                    if a == 1 and b == 1:
                        print(f"x²+x+{c} = 0")
                    else:
                        print(f"{a}x²+x+{c} = 0")
                else:
                    print(f"{a}x²+{b}x+{c} = 0\033[0m")

                quadratic_formula(a, b ,c)

            except:
                print("Please Enter a Number!")

        else:
            print("""\033[91mPlease Enter a Valid choice
\033[93mtype(leave, exit, no) to exit
type(yes or solve) to continue\033[0m""")