#May 5, 2024 




def meters(h):
    #convert height in cm into m
    return h / 100

def BMI(w, h):
    return w / meters(h) ** 2
    




while True:
    try:
        mass = float(input("Enter your weight: "))
        height = float(input("Enter your height: "))

    
    
        print(f"Your BMI is {round(BMI(mass, height), 1)} kg/m²")
                
        if BMI(mass, height) < 18.5:
            print("Underweight")

        elif BMI(mass, height) >= 18.5 and BMI(mass, height) <=24.9:
            print("Normal")

        elif BMI(mass, height) >= 24.9 and BMI(mass, height)<= 29.9:
            print("Overweight")

        else:
            print("Obese")
    except:
        print("Please Enter a Number")