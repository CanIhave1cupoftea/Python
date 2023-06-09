#April 20, 2023
#Simple minute passed calculator with a maximum of 1 hour and 59 minutes

def minutes_passed(i, f):
    min = f - i
    if f < i:
        min = (f + 1440/2) - i
        if min >= 60:
            hr = min // 60
            min = min % 60
            if hr == 1 and min > 1:
                print(f"{hr} hour and {min} minutes has passed\n")
                return hr
            elif hr == 1:
                print(f"{hr} hour has passed")
                return hr
            
            elif hr > 1 and min == 1:
                print(f"{hr} hours and {min} minute has passed\n")
                return hr
            else:
                print(f"{hr} hours and {min} minutes have passed\n")
                return hr

        else:
            print(f"{min} minutes have passed\n")
            
    else:
        print(f"{min} minutes have passed\n")


while True:
    
    print("Enter Initial Time Value: ")
    time_0 = input("")
    minfind_0 = time_0.find(':')
    min_0 = time_0[minfind_0+1:]

    print("Enter Final Time Value: ")
    time_1 = input("")
    min_find_1 = time_1.find(':')
    min_1 = time_1[min_find_1+1:]

    if ':' not in time_0 or ':' not in time_1:
        print("Please Enter a Valid Time\n")
    
    elif '-' in time_0 or '-' in time_1:
        print("Please Enter a Valid Time\n")    

 
    else:
        
        try: 

            i = int(min_0)
            l = int(min_1)               
        

            if i <= 59 or l <= 59:
                minutes_passed(i,l)
        except:
            print("Please Enter Valid Timeads")
        