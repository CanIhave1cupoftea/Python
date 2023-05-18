#May 16,2023

#Dec to Bin
def binary(num):
    bin = []
    current = list(num)
    current.reverse()
    for i in range(len(num)):
        if current[i] == '1':
            bin.append(2 ** int(i))
    
    return sum(bin)
print(binary('11111110001011'))

#Dec to Oct
num = 10
octa = []
while num > 0:
    octa.append(str(num % 8))
    num //= 8

octa.reverse()
print("".join(octa))

#Dec to Hexa




decimal = 170
binary = []
while decimal > 0:
    binary.append(str(decimal % 2))
    decimal //= 2
binary.reverse()
print("".join(binary))
