import os
import random  # Imports random #
os.system('cls' if os.name == 'nt' else 'clear')


def rpsGame():

    botMove = random.randrange(0, 3) + 1  # Generates bot move #

    def player():  # Player move function #\
        global playerMove
        playerMove = input("\n player turn: ")
        # When player plays 'r' #
        if playerMove == "r":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("player played rock")
            # When player plays 'p' #
        elif playerMove == "p":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("player played paper")
            # When player plays 's' #
        elif playerMove == "s":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("player played scissors")
            # When player plays 'other' #
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("that isnt a legal move, pick again")
            player()

        bot()

    def bot():  # Bot Move Function #
        # When bot rolls 0 #
        if botMove == 1:
            print("\nbot played rock")
            # When bot rolls 1 #
        if botMove == 2:
            print("\nbot played paper")
            # When bot rolls 2 #
        if botMove == 3:
            print("\nbot played scissors")
        win()

    def win():  # Win Function #
        ### Player Win ###
        if playerMove == "r" and botMove == 3:
            print("\nPlayer wins!")

        elif playerMove == "p" and botMove == 1:
            print("\nPlayer wins!")

        elif playerMove == "s" and botMove == 2:
            print("\nPlayer wins!")

            ### Bot Win ###
        if playerMove == "r" and botMove == 2:
            print("\nBot wins!")

        elif playerMove == "p" and botMove == 3:
            print("\nBot wins!")

        elif playerMove == "s" and botMove == 1:
            print("\nBot wins!")

            ### Tie ###
        if playerMove == "r" and botMove == 1:
            print("\nIt's a tie!, no one wins.")

        elif playerMove == "p" and botMove == 2:
            print("\nIt's a tie!, no one wins.")

        elif playerMove == "s" and botMove == 3:
            print("\nIt's a tie!, no one wins.")
        input("\nPlay again: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        rpsGame()

    player()


rpsGame()
