import os
from queue import Full
os.system('cls' if os.name == 'nt' else 'clear')

playing = True
free = 0
player = 1
win = False
# Board #
Board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

while (playing):

    for p in range(6):
        print(Board[p])

    Move = int(input('your move: '))

    # Moves #
    def move():
        global player
        # Column Full #
        if Board[0][Move - 1] != free:
            os.system('cls' if os.name == 'nt' else 'clear')
            player += 1
            print("That column is full, pick a new one")
        else:
            for r in range(5, -1, -1):
                if Board[r][Move - 1] == free:
                    Board[r][Move - 1] = player

                    break
            os.system('cls' if os.name == 'nt' else 'clear')

    def win():
        global win, player
        # Check - Horizontal Line #
        for x in range(7 - 3):
            for y in range(6):
                if Board[y][x] == player and Board[y][x+1] == player and Board[y][x+2] == player and Board[y][x+3] == player:
                    print("Player", player, "wins")
                    for p in range(6):
                        print(Board[p])
                    win = True
        # Check | Vertical Line #
        for y in range(7):
            for x in range(6 - 3):
                if Board[x][y] == player and Board[x+1][y] == player and Board[x+2][y] == player and Board[x+3][y] == player:
                    print("Player", player, "wins")
                    for p in range(6):
                        print(Board[p])
                    win = True
        # Check \ Diagonal Line #
        for y in range(7 - 3):
            for x in range(6 - 3):
                if Board[x][y] == player and Board[x + 1][y + 1] == player and Board[x + 2][y + 2] == player and Board[x + 3][y + 3] == player:
                    print("Player", player, "wins")
                    for p in range(6):
                        print(Board[p])
                    win = True
        # Check / Diagonal Line #
        for x in range(6 - 3):
            for y in range(3, 6):
                if Board[x][y] == player and Board[x + 1][y - 1] == player and Board[x + 2][y - 2] == player and Board[x + 3][y - 3] == player:
                    print("Player", player, "wins")
                    for p in range(6):
                        print(Board[p])
                    win = True
        # Check Tie #
        if 0 not in Board[0]:
            print("No one wins")
            for p in range(6):
                print(Board[p])
            win = True

    if 1 <= Move <= 7:
        move()
        win()
        player += 1
        if player == 3:
            player = 1
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("That is'nt a legal move, try again")
    # Close After Game Ends #
    if win == True:
        os.system("pause")
        exit()
