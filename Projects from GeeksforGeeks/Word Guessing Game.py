#June 10, 2023
#Making word guessing game in python
#The user has to guess letters from the alphabet until he can guess the entire word correctly

from random import choice
words = ["dinosaur", "shark", "megalodon"]
word = choice(words)
letters = []
lives = 10



while lives > 0:
    guessed = True
    for char in word:

        if char in letters:
            print(char, end='')

        else: 
            print("_", end="")
            guessed = False

    print()
    if guessed:
        print("Congratulations! You guessed it!")
        break

    
    try:

        letter = input("Guess a letter: ")
        assert len(letter) == 1, "Enter 1 letter at a time"
        assert letter.isalpha(), "Please Enter letters only"
        letters.append(letter)

        if letter not in word:
            lives -= 1
            print("Try Again!")
            if lives == 1:
                print(f"Oh no! You only have {lives} life! This is your last chance")
            
            elif lives == 0:
                print("You ran out of lives")
                print(f"The word is: {word}")
                break

            else:
                print(f"You have {lives} more lives")
                
    except AssertionError as e:
        print(e)

   