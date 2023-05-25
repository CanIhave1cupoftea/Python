#May 18, 2023 - 8:30pm - I got pretty carried away in competitive programming, - Continuing this, May 20, 2018 - 8:45pm
#Making a library system
#Issued Books, Fave books, Return Books


def menu(l):
    print("LIBRARY".center(30, "="))
    for i, j in enumerate(l):
        
        print(f"{i+1}. {j}")

mainmenu = ["View Books", "Favorite Books", "Return Books", "Exit"]
avail = ["Lord of the Rings", "The Song of Ice and Fire"]
borrowed = ["The Compound Effect", "Atomic Habits"]
borrow_add = ["Borrow", "Add to Favorite"]
favorite = []
avail.extend(borrowed)
while True:
    menu(mainmenu)
    print("".center(30, "="))
    user = input("What do you want to do? ")
    print()
    if user == "1":
        print("Bookshelf".center(30, "="))
        for num, books in enumerate(avail):
            if books in borrowed:
                print(f"{num+1}. {books.center(30)} - Borrowed")
            else:
                print(f"{num+1}. {books.center(30)} - Available")
        print(f"{num+2}. Back")
        user = input("What do you want to do? ")
        if int(user) < len(avail): 
            choice = avail[int(user)-1]
            print(choice.center(30,"="))
            if choice in borrowed:
                print("1. ",borrow_add[1])
                print("2. Go back")
                user = input("What do you want to do? ")
                if int(user) == 1:
                    favorite.append(choice)
                    print(f"Added {choice} to your favorites")
                    
            else:
                for i, j in enumerate(borrow_add):
                    print("{}. {}".format(i+1, j))
                print("3. Go back")
                user = input("What do you want to do? ")
                if int(user) == 1:
                    borrowed.append(choice)
                    print(f"Succesfully borrowed {choice}")
                elif int(user) == 2:
                    favorite.append(choice)
                    print(f"Added {choice} to your favorites")

    elif user == "2":
        print("Favorites".center(30, "="))
        if favorite == []:
            print("No favorites added yet.")
            print(f"1. Go Back")
        else:
            for num, books in enumerate(favorite):
                print(f"{num+1}. {books.center(30)}")
            print(f"{num+2}. Go Back")
        user = input("What do you want to do? ")

            
    elif user == "3":
        print("Books Issued".center(30, "="))
        for num, books in enumerate(borrowed):
            print(f"{num+1}. {books.center(30)}")
        user = input("Which Book??")
        borrowed.pop(int(user)-1)
        print("Book Successfully Returned")
    elif user == "4":
        print("ADIOS!")
        quit()

