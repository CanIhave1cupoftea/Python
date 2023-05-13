#getting the time and half pay of employees
def computepay(h, r):
    if h > 40:
        gpay = (40*r)+(h-40)*(r*1.5)
    else:
        gpay = h*r
    return gpay

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Your Rate: "))
p = computepay(hrs, rate)
print("Your Total Pay is", p)


