#May 14, 2023
# some practice regarding collections/ sequence data types in python
# a collection or sequence is just like a variable that can store multiple data regardless of data types

#first we have list
#a list is mutable(changeable), ordered(each place has index and does not change unless modified)
#there are duplicates in list
#I will make a grocery list


"""
groceries = []

#we will have the user to input what the user wants
while True:
    user_choice = input("Enter an item you want to buy(q to quit, e if it is enough)").lower()
    if user_choice == "q":
        quit()
    
    elif user_choice == "e":
        break
    else:
        groceries.append(user_choice)
#after the user has input all of grocery items, we will print the grocery lsit we made for the user
print("Here's your grocery list:".center(30, "="))
count = 1
for items in groceries:
    print(f"{count}. {items}")
    count += 1
print("".center(30, "="))

"""

#we will create a list that will compare itself to another lits to see if we have duplicated items

"""items = []
surplus = []
while True:
    user = input("Enter some item into our toolbox(0 to stop): ")
    if user == "0":
        break
    if user not in items:
        items.append(user)    
    else:
        surplus.append(user)
print(items)
print(surplus)
"""

#end
#next, we have tuples
#tuples are ordered but immutable(cannot be changed, once made)
