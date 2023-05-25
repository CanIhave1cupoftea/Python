#May 18, 2023
#Practicing the idea of iterables(string, lists, range and so on)
#Iterable is a series of any values
# we can use 2 functions when working with iterables, filter(), map()

#Filter(function, iterable)
#Filter is used to focus on specific values on an iterable
#creating a lambda function to filter out the even numbers on a given list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = lambda x:x % 2 == 0

print(list(filter(even, list1)))

#Map(function, iterable)
#Map is used when you want to modify values on an iterable
#creating a lambda function that raises a number by the power of 2 and combining it with map function in order to have all the numbers on the list squared

expo = lambda x:x ** 2
print(list(map(expo, list1)))

import pandas 

