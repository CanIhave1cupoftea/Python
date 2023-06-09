while True:
    line = input('> ')
    if line == 'done':
        break
    if line[0] == '#':
        continue
    print(line)
print('Done')

#definite loops

for i in [5,4,3,2,1]:
    print(i)
print('Finish')


alpha = ()
for letter in alpha:
    print(letter)

friends = ['Joseph', 'John', 'Renz']
for friend in friends:
    print("Hi", friend)
print('done')

#Find the largest num
largest = 0
print("Before, ", largest)
for any_num in [3, 5, 15, 2, 60, 89, 93, 5, 10]:
    if any_num > largest:
        largest = any_num
    print(largest, any_num)
print("After, ", largest)

#counting loops
count = 0
for num in [10, 20, 39,89, 10, 23, 56]:
    count = count + 1
    print (count, num)
print("Total:",count)

#Summing in a loop
sum = 0
print("Before summing up", sum)
for num in [12, 123, 89, 9, 89, 32 , 32]:
    sum = sum + num
    print(num, sum)
print("After summing up", sum)

#simple not complex definite fibonacci sequence using for loop
fibonacci = 0
for sequence in [0, 1, 1, 2, 3]:
    fibonacci = fibonacci + sequence
    print(fibonacci)

#filter for a loop

for value in [1,3,5,7,8,12,56,7]:
    if value > 20:
        print("WOW", value)

#searching through boolean values in a loop

test = False
for num in [35, 60, 100, 56, 19]:
    if num == 60:
        test = True
    print(test, num)

#Find the smallest num
smallest = None
print("Before", smallest)
for any_num in [3, 5, 15, 2, 60, 89, 93, 5, 10]:
    if smallest is None:
        smallest = any_num
    elif any_num < smallest:
        smallest = any_num
    print(smallest, any_num) 
print("After", smallest)

#maximum and minimum checker with user input
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        istr = int(num)
    except:
        print("Invalid Input")

    #if smallest is None:                                        
    #   smallest = istr
    #elif smallest > istr:
    #    smallest = istr
    #if largest is None:
    #   largest = istr
    #elif largest < istr:
    #   largest = istr
    
    if largest is None:
        largest = istr
    elif istr > largest:
        largest = istr
    if smallest is None:
        smallest = istr
    elif istr < smallest:
        smallest = istr

print("Maximum is", largest)
print("Minimum is", smallest)


tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)  
    
    


