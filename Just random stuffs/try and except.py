rawstr = input("Enter A Number: ")

try:
    val =   int(rawstr)
except:
    val = -1

if val > 0:
    print("That is a number")
else:
    print("That is not a number")

#Grading System
score = input("Enter Score: ")

try:
   scr = float(score)
except:
   scr = -1
    
if scr >= 0.9 and scr <= 1.0:
    print("A")
elif scr >= 0.8 and scr < 0.9:
    print("B")
elif scr >=0.7 and scr < 0.8:
    print("C")
elif scr >= 0.6 and scr < 0.7:
    print("D")
elif scr >= 0.0 and scr < 0.6:
    print("F")
else:
    print("ERROR")