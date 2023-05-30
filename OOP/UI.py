#May 26, 2023 12:49pm = 1:10pm
#making a function that will enumerate my UI for me


def menu(arr):
    if isinstance(arr, list):
        for k, i in enumerate(arr):
            print(''.join(f"{k+1}. {j}" for j in i.keys()))
    
    elif isinstance(arr, dict):
        for key in arr:
            arr[key].append("Back")
        for i in arr:
            for k, j in enumerate(arr[i]):
                print(f"{k+1}. {j}")
           
def user():
    inp = input("What would you like to do? ")
    return int(inp)

mainmenu = [{"Play": ["New Game", "Load Game", "Delete Game"]}, 
            {"Options": ["Volume", "Brightness", "Difficulty"]}, 
            {"Quit": ["Quit"]}
            ]

a = "hi"
eval(a)
