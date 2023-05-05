#greetings lang=parameter es fr and tg are arguments that will replace the parameters
def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    elif lang == "tg":
        return "Kumusta"
    else:
        return "Hello"


language = input("What language do you speak? ")
name = input("Enter your name: ")
print(greet(language), name)


def pay(hour, rph):
    pay = hour * rph
    return pay

#getting the time and half pay of employees
def computepay(h, r):
    if h > 40:
        gpay = (40*r)+(h-40)*(r*1.5)
    else:
        gpay = h*r
    return gpay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Your Rate: "))
p = computepay(hrs, rate)
print("Pay", p)
