#May 27, 2023
#Making a binary search algorithm
#A binary search algorithm is effective on sorted data structures, it will search inside of it and goes right into the middle, splitting it until the data is found


sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]


count = 0
while True:
   
    half = len(sample)//2
    count+=1
    if element == sample[half]:
        print("Found")
        break
    elif element < sample[half]:
        sample = sample[sample[half]-1::-1]
        count+=1

    else:   
        sample = sample[sample[half]-1:]
        count+=1


print(count)

