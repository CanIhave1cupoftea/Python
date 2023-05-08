#May 6, 2023 - May 7, 2023 10:47pm
#Random number picker with maximum of 5 players!

import random

def random_play(player):
        print("\033[1mEnter 0 to go back to the Main Menu\033[0m")
        choice = int(input("What is the number limit? "))
        if choice == 0:
            print("Going back to Main Menu...")
            main()
        while choice <= player:
            print("\033[91mThe limit must not be less or equal to the number of players!\033[0m")
            choice = int(input("What is the number limit? "))
        random_num = random.randint(1, choice)
        pseudo_player = 1
        player_choice = 1
        number = []
        while pseudo_player <= player:
            try:
                number_choice = int(input("Player", pseudo_player, "please enter your number: "))
                if number_choice <= 0:
                    print("\033[91mNegative numbers or 0 are not allowed as your number\033[0m")
                    continue

                elif number_choice > choice:
                    print("""\033[91mThe number you've entered exceeds the limit!
    \033[1m\033[95m(Enter 0 to reset the limit)\033[0m""")
                    number_choice = int(input(f"Player {pseudo_player} please enter your number: "))

                    if number_choice == 0:
                        choice1 = int(input("Set the new number limit: "))
                        while choice1 == choice:
                            print("\033[91mThat's already the set limit!")
                            choice1 = int(input("Set the new number limit: "))
                        if choice1 == 0:
                            print("You cancelled changing the limit")
                            continue
                        
                        else:
                            print(f"\n\033[1m=======New Number Limit is: {choice1}=======\033[0m\n")
                        
                        while choice1 <= player:
                            print("\033[91mThe limit must not be less or equal to the number of players!\033[0m")
                            choice1 = int(input("Set the new number limit: "))
                        pseudo_player = 1
                        number.clear()
                        choice = choice1
                        
                    else:
                        if number_choice not in number:
                            number.append(number_choice)
                            pseudo_player += 1
                        else:
                            print("\033[91mThat number is already taken! Enter another number\033[0m")
                            continue
                    
                else:
                    if number_choice not in number:
                        number.append(number_choice)
                        pseudo_player += 1
                    else:
                        print("\033[91mThat number is already taken! Enter another number\033[0m")
                        continue
            except: 
                print("Please Enter a Number")
                continue     
        print(f"\033\n[1m=========Number Limit==> {choice} <===========\033[0m")
        print(f"""\033[1m\033[94m  ===========LUCKY NUMBER===========
 \033[1m\033[36m  =============| {choice} |=============\033[0m\n""")
               
        for num_choice in number:
            if num_choice == random_num:
                print(f"""            \033[92mPlayer {player_choice}: {num_choice}\033[0m""")
            else:
                print(f"""            \033[91mPlayer {player_choice}: {num_choice}\033[0m""")
            player_choice += 1
            
                
        try:
            position = number.index(random_num)+1
            print("""\n\033[92m♦~~~~~~~~♦~CONGRATULATIONS!~♦~~~~~~~~♦\033[0m""")
            print(f"""            \033[1m\033[95mPLAYER {position} WINS\n\033[0m""")
        except:
            print("\n\033[1m\033[91m=========BETTER LUCK NEXT TIME=========\033[0m")
            print("Awww too bad, nobody got it but you can try again!")
    
        game_choice = input("Do you wanna play again? ")
        if (game_choice == "yes" or game_choice =="Yes") or (game_choice == "YES" or game_choice == "Y") or game_choice == "y":
            random_play(player)
        elif game_choice == "no":
            print("\033[92mTHANK YOU FOR THE PLAYING THE GAME!\033[0m")
            quit()
        else:
            print("\033[92mTHANK YOU FOR THE PLAYING THE GAME!\033[0m")
            quit()

def play():
    while True: 
        try:
            players = int(input("\033[0m\033[93mHow many players will play? (Upto 5 players only): \033[0m"))
            
            if players == 0:
                print("\033[92mTHANK YOU FOR PLAYING THE GAME!\033[0m")
                break
            elif players < 2:
                print("\033[91mAtleast 2 players are needed to play this game\033[0m")
                continue
            elif players > 5:
                print("\033[91mMaximum of 5 players only\033[0m")
                continue
                
            else:
                random_play(players)
        except:
            print("\033[91mPlease Enter a Number or You Can Enter '0' to Immediately Quit the Game\033[0m ")
            continue
def main():
    while True:
        print("\033[96m\033[1m|=====LUCKY GAME!=====|")
        print("""|1. \033[92mPlay\033[0m\033[96m              |  
|2. \033[91mQuit\033[0m\033[96m              |
|=====================|\033[0m""")
        play_or_quit = input("What do you want to do? \033[92m")

        if play_or_quit == "1": 
            print("\033[92mHave Fun Playing!\033[0m\n")
            play()
                
        elif play_or_quit == "2":
            yes_or_no = input("Are you sure you want to quit?")
            if (yes_or_no == "yes" or yes_or_no =="Yes") or (yes_or_no == "YES" or yes_or_no == "Y") or yes_or_no == "y":
                print("\033[92mTHANK YOU FOR THE PLAYING THE GAME!\033[0m")
            elif (yes_or_no == "no" or yes_or_no =="No") or (yes_or_no == "NO" or yes_or_no == "N") or yes_or_no == "n":
                continue
        else: 
            print("\033[mPlease Enter Only the Corresponding Number\033[0m")
            continue
                
main()
