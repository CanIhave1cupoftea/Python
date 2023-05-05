import math

while True:
    
    try:
        print("""\033[1m\033[92m=================Circumference of a Circle=================
            \033[91m(Type 'exit' to close the program)               \033[0m""")
        
        radius = input("Enter the Radius: ")
        if radius != 'exit':
            radius = float(radius)
            circumference = 2 *math.pi * radius
            print(f"The Circumference of the Circle is: {round(circumference, 2)}cm")

        else:
            print("\033[93mTHANK YOU FOR USING THE CIRCUMFERENCE CALCULATOR!!!\033[0m]")
            break
                    
    except:
        print("Enter a Number")
        continue
    else:
        print("\033[1m\033[92m===========================================================\033[0m")

    while True:
        choice = input("Do you want to try again? ")
        if choice == "yes":
            break
        
        elif choice == "no":
            print("THANK YOU FOR USING THE CIRCUMFERENCE CALCULATOR!!!")
            quit()

        else:
            continue
        
    
        
