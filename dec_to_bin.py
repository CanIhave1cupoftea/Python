#May 16, 2023
#decimal to binary

decimal = 170
hexa = []
while decimal > 0:
    hexa.append(str(decimal % 16))
    decimal //= 16
hexa.reverse()
final = "".join(hexa)
print(final.translate(final.maketrans({"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"})))



    
