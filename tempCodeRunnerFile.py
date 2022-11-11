def bot(playerNum):
        player_turn = False
        global bn
        global total
        bn = random.randrange(1, 4)
        print(bn)
        totalNum(playerNum, bn)