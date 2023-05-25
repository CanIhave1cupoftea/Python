#May 19, 2023 10:13pm
#Fibonnacci sequence, a fibonacci sequence is the sum of the 2 previous numbers whcih defines the next number

fibonacci = []
#multi assignment
a, b = 0, 1
while a < 10:
    fibonacci.append(a)
    #swapping the values and assiging new one for b
    a, b = b, a + b

print(fibonacci)
