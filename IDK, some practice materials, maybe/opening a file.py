#May 14, 2023 2:50pm
#opening and reading a file using python

#This one detects if a file or folder exist and also check if it is a file or a directory
"""import os

item = "E:\Programming\Python\My Projects\Python\IDK, some practice materials, maybe"

if os.path.exists(item):
    print("This file exist")
    if os.path.isfile(item):
        print("This is a file!")
    elif os.path.isdir(item):
        print("This is a directory/folder")


else:
    print("This file does not exist")"""

#This one reads the file
try:

    with open("sample.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("file not found")

#This one writes on a file, I am using text files as a sample

with open('sample.txt') as file:
    print(file.read())
