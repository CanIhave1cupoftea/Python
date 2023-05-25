#May 22, 2023
#I will make a library system using classes

class Books:

    count_of_books = 0

    def __init__(self, name, author, status) -> None:

        self.name = name
        self.author = author
        self.status = status
        
        
    @classmethod
    def addBooks():
        count_of_books += 1

    def seeName(self):
        return self.name
    
    def seeAuthor(self):
        return self.author
    
    def seeStatus(self):
        return self.status
    
    def seeDetails(self):

        return f"Name: {self.name}\nAuthor: {self.author}\nStatus: {self.status}"

    
book1 = Books("LOTR", "JRR Tolkien", "Available")
book2 = Books("Thus Spoke Zarathustra", "Friedrich Nietzhce", "Borrowed")

print(Books.count_of_books)

        
