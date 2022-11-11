import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
game = True
player_turn = False
total = 0

if game == True:
    def check21(total):

        if total >= 21 and player_turn == True:
            print("u lose!")
            os.system("pause")
            exit()
        elif total >= 21 and player_turn == False:
            print("You win!")
            os.system("pause")
            exit()
        else:
            print("keep going")
        print(total)
        player()

    def player():
        player_turn = True
        global pn
        pn = int(input("Enter a number from 1-3: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pn)
        bot(pn)

    def bot(playerNum):
        player_turn = False
        global bn
        global total
        bn = random.randrange(1, 4)
        print(bn)
        totalNum(playerNum, bn)

    def totalNum(playerNum, botNum):
        global total
        total = total + (playerNum + botNum)
        check21(total)

    player()
