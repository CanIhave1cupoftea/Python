def min_to_hour():
    
    while True:
        hr = 0
        min = 0
        sec = 0

        try:
            time = int(input("Enter the Desired Hour: "))
        except:
            print("Enter a number")
            continue

        #while hour < time:
        while sec != 59:
            for second in range(1,60):
                sec = second
                print(sec)

        else:
            sec = 0
            print(f"{min}:{sec}")

min_to_hour()