#April 19, 2023
#area and volume of a rectangle

def rectangular_area(length, width, height=None):
    if height is None:
        area = length * width
        return area
    else:
        volume = length * width * height
        return volume
    
while True:

    print("Which do you want to find out? area or volume?(Type Exit to Close Program)")
    choice = input("")
    if choice == 'exit':
        quit()

    elif choice == 'area':
        while True:
            print("Area of the Rectangle:")
            l = input("Please Enter the Length: ")
            w = input("Please Enter the Width: ")
        
            try:
                lint = int(l)
                wint = int(w)
                print(f"The Area of the Rectangle is {rectangular_area(lint, wint)}cm²")
            except:
                print("Please Enter a Valid Number")
                continue
            ans = input("Do you want to find out the area again?")
            if ans == 'yes':
                continue
            elif ans == 'no':
                break
            else:
                while True:
                    ans = input("Do you want to find out the area again?")
                    if ans == 'yes':
                        break
                    else:
                        continue

    elif choice == 'volume':
        while True:
            print("Volume of the Rectangle:")
            l = input("Please Enter the Length: ")
            w = input("Please Enter the Width: ")
            h = input("Please Enter the Height: ")
            try:
                lint = int(l)
                wint = int(w)
                hint = int(h)
                print(f"The Volume of the Rectangle is {rectangular_area(lint, wint, hint)}cm³")
            except:
                print("Please Enter a Valid Number")
                continue
            ans = input("Do you want to find out the volume again?")
            if ans == 'yes':
                continue
            elif ans == 'no':
                break
            else:
                while True:
                    ans = input("Do you want to find out the volume again?")
                    if ans == 'yes':
                        break
                    else:
                        continue
                
    else:
        print("Please choose only between the two, area and volume\n")
            



            