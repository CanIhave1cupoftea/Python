#May 27, 2023
#idk, just trying to come with some practice and I think creating an account would be challenging

acc = {}

user = input("Username: ")
password = input("Password: ")
acc[user] = password


choice = input("Do you want to log-in? ").lower()
if choice == "yes":
    print("Enter Account Details")
    user = input("Enter your account: ")
    if user not in acc.keys():
        print("Username does not exist!")
    password = input("Enter your password: ")

    if acc[user] == password:
        print("You have accessed you account!")
    else:
        print("Wrong password")