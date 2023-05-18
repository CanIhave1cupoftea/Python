#May 16, 2023
#palindrome detector, a palindrome is a word that when reversed still the same word

def palindrome(word):
    glovar = "I am a local variable now"
    print(glovar)
    if word == word[:: -1]:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"

def main():
    while True:
        user = input("Please enter a string: ")
        if not user.isalpha() or len(user) < 2:
            print("Cannot contain spaces or numbers")
            continue
        else:
            print(palindrome(user))
if __name__ ==  "__main__":
    main()
    