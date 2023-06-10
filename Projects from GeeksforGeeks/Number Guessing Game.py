#Create a project where it prompts the user whether his/her guess is lesser of greater then the random number

from random import randint

#random number
random_num = randint(1,100)


#number of guesses
count = 0
#user input
while True:
    user = int(input("Guess the Number: "))

#logic

    if user != random_num:
        print("You guessed to high") if user > random_num else print("You guessed too low")
        count += 1

    else:
        print("You got it!")
        break

print(f"Total number of guesses: {count}")