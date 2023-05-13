#May 11, 2023
#May 13, 2023 7:32am - 9:00am changes
import time 
def duplicate_detector(num):
    no_repeat = set()
    isDuplicate = False
    for number in num:
        if number not in no_repeat:
            no_repeat.add(number)
        else:
            isDuplicate = True

    return isDuplicate
def duplicate_counter(num):
    new_list = []
    duplicates = {}
    for number in num:
        if number not in new_list:
            new_list.append(number)
            numbers = 1
        else:
            numbers += 1
            duplicates[number] = numbers
    
    for numbers, repeat in duplicates.items():
        print(f"Number {numbers} repeated {repeat} times!")
    return
def main():
    flags = 0
    while True:
        nums = []
        if flags == 3:
            flags_2 = 0
            while True:
                last_chance = input("Do you want to quit?? (yes/no) ")
                if last_chance.lower() == "yes":
                    for letter in "THANK YOU!":
                        time.sleep(0.1)
                        print(letter, end="")
                elif last_chance.lower() == "no":
                    flags = 0
                    break
                elif flags_2 == 2:
                    print("You're trippin' BYE~BYE")
                    quit()
                else:
                    print("Enter 'yes' or 'no'")
                    flags_2 += 1
                    continue

        elif flags > 3:
            print("You're trippin' BYE~BYE")
            break


        try:          
            number_choice = int(input("How many numbers do you want to input? "))
            if number_choice >= 3:
                flags_3 = 0
                while number_choice != 0:
                    if flags_3 == 3:
                        last_chance = input("Do you want to quit?? (yes/no) ")
                        if last_chance.lower() == "yes":
                            for letter in "THANK YOU!":
                                time.sleep(0.1)
                                print(letter, end="")
                            quit()
                        elif last_chance.lower() == "no":
                            continue
                        else:
                            print("You're trippin' bruh")
                            quit()
                    try:
                        number = int(input("Enter a Number: "))
                        nums.append(number)
                        number_choice -= 1     
                    except:
                        flags_3 += 1
                        continue
                    
            else:
                flags += 1
                raise ValueError
            
        except ValueError:
            flags += 1
            print("Your choice must be greater than 2 only")
            continue

        if duplicate_detector(nums) == True:
            print("There are duplicates")
            duplicate_counter(nums)
        else:
            print("There are no duplicates")

        question = input("Do you want to input again? (yes/no) ")
        if question.lower() != "yes":
            for letter in "THANK YOU!":
                time.sleep(0.1)
                print(letter, end="")
        else:
            continue

if __name__ == "__main__":
    main()

    