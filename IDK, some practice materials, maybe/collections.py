#May 19, 2023
#understanding a little bit more about collections

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


#Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection: I got this from python documentation
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


#Given two lists a, b. Check if two lists have at least one element common in them.
def common_element(a, b):
    a = set(a)
    b = set(b)

    return True if a.intersection(b) else False

a = [1, 2, 3, 4, 5]
b = [0, 6, 7, 8, 9]

#method 2, using any
def any_element(a, b):
    return any(i in a for i in b)

print(any_element(a, b))

#method 3 traversing a list
def traverse_element(a, b):
    return any