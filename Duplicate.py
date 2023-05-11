def duplicate_detector(num):
    if num == None:
        nums = []
        nums.append(num)
        no_repeat_number = []
        while num not in nums:
            nums.append(num)
        print(nums, num)
        

    for n in nums:
        if n in no_repeat_number:
            return True
        no_repeat_number.append(n)
    return False
number_choice = int(input("How many numbers do you want to input? "))
while number_choice != 0:
    number = int(input("Enter a Number: "))
    number_choice -= 1
print(duplicate_detector(number))

    