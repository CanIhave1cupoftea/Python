#May 11, 2023 6:57pm - 7:20pm
#Compund Interest Calculator
#formula a = p(1+r/n)^t

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal can't be less than or equal to 0")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        principal("Interest can't be less than or equal to 0")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        principal("Time can't be less than or equal to 0")

A = principal * pow((1+rate/100), time)
print(f"Balance after {time} year/s: {A:.2f}")
