#May 12, 2023 7:14am 7:40am
#counting how many prime numbers are there between 1 and n

def prime_count(num):
    if num <= 0:
        print("There are no prime numbers")

    prime_numbers = 0
    for numbers in range(1, num+1):
        factors = 1
        if numbers > 1:
            for i in range(2, numbers+1):
                if numbers % i == 0:
                    factors += 1
            if factors <= 2:
                prime_numbers += 1
    print("There are {prime} prime numbers between 1 and {number_choice}".format(prime=prime_numbers, number_choice=num))
print('{:^50}'.format("Welcome to Prime Number Counter!"))
print("(The Bigger the number input, the slower the program)".center(50))
while True:
    try:
        choice = int(input("Enter the number: "))
        if choice == 1 or choice <= 0:
            print("There are no prime numbers between 1 and below")
        else:
            prime_count(choice)
            question = input("Do you want to input again? ")
            while question.lower() != "yes":
                if question.lower() == "no" :
                    quit()
                else:
                    question = input("Do you want to input again? ")
            
            else:
                continue
    except ValueError:
        print("Please Enter a Valid Number")
        continue

                


            
