#May 25, 2023
#dunder methods or magic methods, enclose by double underscores

class Word:

    def __init__(self, word):

        self.word = word

    def __repr__(self) -> str:
        
        return self.word
    
    def __add__(self, additional):

        return self.word + " " +    additional

class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print "Base1"