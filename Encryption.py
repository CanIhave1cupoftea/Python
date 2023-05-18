#May 13, 2023 3:41pm - 4:11pm
#Encrypting a user input

import random
import string

chars = string.ascii_letters + string.punctuation + " " + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

user = input("Enter a message to encrypt: ")
encrypted = ""

for letter in user:
    index = chars.index(letter)
    encrypted += key[index]
    
print(f"You Entered: {user}\nEncrypted Mesage: {encrypted}")
