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

"""
def collatz(number=int):
    return number // 2 if number % 2 == 0 else 3 * number + 1

print(collatz(3))"""


import random, time, copy

h = 50
w = 20

cells = []
for x in range(w):
    col = []
    for y in range(h):
        if random.randint(0,1) == 0:
            col.append('#')
        else:
            col.append(' ')
    cells.append(col)

while True:
    print('\n\n\n\n\n\n\n')
    current = copy.deepcopy(cells)

    for y in range(h):
        for x in range(w):
            print(current[x][y], end='')
        print()
    
    for x in range(w):
        for y in range(h):
           

            leftCoord  = (x - 1) % w
            rightCoord = (x + 1) % w
            aboveCoord = (y - 1) % h
            belowCoord = (y + 1) % h

            # Count number of living neighbors:
            numNeighbors = 0
            if current[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if current[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if current[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if current[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if current[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if current[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if current[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if current[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if current[x][y] == '#' and (numNeighbors == 2 or
        numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                cells[x][y] = '#'
            elif current[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                cells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                cells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.


