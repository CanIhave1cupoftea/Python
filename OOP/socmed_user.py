class Socialite:

    def __init__(self, f_name, l_name, likes, friends):
        self.name = "{} {}".format(f_name.capitalize(), l_name.capitalize()) 
        self.likes = likes
        self.friends = friends
    
    def intro(self):
        print(f"Hello, I am {self.name}")
    
    def seeProfile(self):
        print(f"Full name: {self.name}")
        print(f"Likes: {self.likes}")
        print(f"Friends: \n-" + "\n-".join([i for i in self.friends]))

person = Socialite("Henry", "Moreno", 129, ["Renz", "Jim", "Jam", "Karl", "Rek"])
print(person.likes)
person.intro()
person.seeProfile() 