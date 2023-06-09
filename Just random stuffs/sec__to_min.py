def minute_count():
    while True:
        minute = 0
        second = 1
        try:
            timer = int(input("How Many Minutes Do you want to Count?: "))

            if timer > 60 or timer < 0:
                print("Invalid Number")
                continue


        except:
            print("Please Enter a number")
            continue

        while minute != timer:
            
            if minute >= 1:
                
                print(f"{minute}:{fill_sec}")
                second += 1
            
            else:
                print(second)
                second += 1

            while second == 60:
                second = 0 
                minute += 1
            conv_sec = str(second)
            fill_sec = conv_sec.zfill(2)
            
        else:
            print(f"{minute}:{fill_sec}")

minute_count()



