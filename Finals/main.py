#June 7, 2023
#Stall Category Information

stalls = []

def create(name):
    return stalls.append(name)

def update():
    print(stalls)
    to_update = input("Please enter a stall name to update: ")
    stalls.remove(to_update)
    new = input("Enter a new stall: ")
    stalls.append(new)
    return "Succesfully updated"

def read():
    return stalls

def delete():
    to_remove = input("Please enter a stall name to remove: ")
    return stalls.remove(to_remove)


print(stalls)
user = input("Please enter stall name")
create(user)
print(read())
print(update())
print(read())
