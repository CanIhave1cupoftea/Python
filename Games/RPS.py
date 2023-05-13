#May 13, 2023 11:26am -1:50pm
#Rock, Paper Scissors game!
import random
import time
def conversation(victor):
    win = ("\033[95mI'll get you next time!\033[0m", 
           "\033[95mI was so close...\033[0m", 
           "\033[95mYou just got lucky\033[0m", 
           "\033[95mNooooo!\033[0m", 
           f"\033[95mI'll play {random.choice(['scissors', 'rock', 'paper'])} this time\033[0m", 
           "\033[95mThis ain't over, better watch out\033[0m", 
           "\033[95mWoah, I wasn't expecting that\033[0m", 
           "\033[95mDon't celebrate too early\033[0m", 
           "\033[95mIt's not over until I win!\033[0m"
)
    lose = ("\033[95mHAHA! Gotcha!\033[0m", 
           "\033[95mWell, I guess luck is on my side this time\033[0m", 
           "\033[95mDo better next time\033[0m", 
           "\033[95mEZ PZ!\033[0m", 
           "\033[95mWant a handicap?\033[0m", 
           "\033[95mDo you know what a sack is? SACK ON DZNUTZ!\033[0m", 
           "\033[95mTrain first before challenging me\033[0m", 
           "\033[95mOOPS, sorry! I think I overdid it\033[0m", 
           "\033[95mI got too serious, my bad\033[0m",
           "\033[95mSHEEEEESH!!! I WIN!\033[0m"
            )
    
    draw = ("\n\033[95mA draw?! What a bummer\033[0m", 
           "\033[95mAre you copying me??\033[0m", 
           "\033[95mYou're lucky it's a draw\033[0m", 
           "\033[95mIT'S A TIE\033[0m", 
           "\033[95mDon't copy me bruh\033[0m", 
           "\033[95mIf it's a draw again, I'm gonna quit! hehe just kidding\033[0m", 
           "\033[95mIf this ain't a draw, I'm probably the winner\033[0m", 
           "\033[95mDoes it ever drive you crazy? Just how fast the night.. changes\033[0m"
    
            )
    
    print("\033[95mENEMY: \033[0m", end="")
    if victor == True:
       for i in random.choice(win):
        time.sleep(0.07)
        print(i, end="")
    
    elif victor == "draw":
       for i in random.choice(draw):
        time.sleep(0.07)
        print(i, end="")
    
    else:
       for i in random.choice(lose):
        time.sleep(0.07)
        print(i, end="")
    print()
      
def main():
    while True:
        print("\033[1mROCK PAPER SCISSOR GAME!\033[0m".center(50, "="))
        
        choices = ("ROCK", "PAPER", "SCISSOR")    
        enemy = random.choice(choices)
        count = 1   
        for choice in choices:
            print(f"{count}. {choice}".center(12), end=" ")
            count += 1
        print()
        user_choice = input("Enter 1, 2 or 3: (Enter 0 to quit) ")
        def r_p_s(user, enemy):
            victor = False
            
            def win():
                print(f"\033[96mYOU: {user:50}\n\033[95mENEMY: {enemy:50}\n\033[92mYOU WIN!\033[0m")
            def lose():
                print(f"\033[96mYOU: {user:50}\n\033[95mENEMY: {enemy:50}\n\033[91mYOU LOSE!\033[0m")

            if (user == "1" or user == "2") or (user == "3" or user == "0"):
                if user == "0":
                    for i in random.choice(("\033[1mTHANKS FOR PLAYING!\033[0m", "\033[1mTHANK YOU FOR PLAYING THE GAME!\033[0m", "\033[1mTHANKS! I HOPE YOU'LL PLAY AGAIN SOMETIME\033[0m")):
                            time.sleep(0.09)
                            print(i, end="")
                    quit()
                else:   
                    
                    print("\n\033[95mENEMY IS THINKING\033[0m", end= "")
                    for load in range(3):
                        time.sleep(0.5)
                        print(".", end="")
                    print()
                    print()
                    user = choices[int(user)-1]
                    if user == "ROCK" and enemy == "SCISSOR":
                        win()
                        victor = True
                    elif user == "ROCK" and enemy == "PAPER":
                        lose()
                    elif user == "PAPER" and enemy =="ROCK":
                        win()
                        victor = True
                    elif user == "PAPER" and enemy =="SCISSOR":
                        lose()
                    elif user == "SCISSOR" and enemy == "PAPER":
                        win()
                        victor = True
                    elif user == "SCISSOR" and enemy == "ROCK":
                        lose()
                    else:
                        victor = "draw"
                        print(f"YOU: {user}\nENEMY: {enemy}")
                        print("DRAW")
                    
                    conversation(victor)
            else:
                print("Select from 1 to 3 only")
        r_p_s(user_choice, enemy)  
        
main()