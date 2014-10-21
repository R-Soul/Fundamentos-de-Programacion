import random
base = [["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]]

def printbase():
    for line in base:
        print (' '.join(line))
    print("")

def inputvalue(turn):
    choice = input("Please choose a cell (via number). ")
    choice = int(choice)
    if base[(choice - 1) // 3][(choice - 1) % 3].isnumeric() == True:
        if turn:
            base[(choice - 1) // 3][(choice - 1) % 3] = "X"
        else:
            base[(choice - 1) // 3][(choice - 1) % 3] = "O"
    else:
        print("Number already taken")
        print("")
        inputvalue(turn)

def calculatescore():
    winner = ""
    for row in range(0,3):
        score = ""
        for num in base[row]:
            score += num
            if score == "XXX":
                winner = "X"
            elif score == "OOO":
                winner = "O"
    for col in range(0,3):
        score = ""
        for row2 in range(0,3):
            score += base[row2][col]
            if score == "XXX":
                winner = "X"
            elif score == "OOO":
                winner = "O"
    if (base[0][0] + base[1][1] + base[2][2]) == "XXX" or base[0][2] + base[1][1] + base[2][0] == "XXX":
        winner = "X"
    elif (base[0][0] + base[1][1] + base[2][2]) == "OOO" or base[0][2] + base[1][1] + base[2][0] == "OOO":
        winner = "O"   
    return winner


def tictactoe():
    printbase()
    counter = 0
    coin = random.randrange(0,2)
    if coin == 0:
        coinr = "LEFT"
    else:
        coinr = "RIGHT"
    print("A coin was flipped, and the winner is the person on the %s." % (coinr))
    print("Person on the %s, please choose a space." % (coinr))
    print("")
    turn = True
    while counter != 9:
        counter += 1
        inputvalue(turn)
        columsum = calculatescore()
        printbase()
        if columsum == "O":
            print ("O Wins!")
            break
        elif columsum == "X":
            print ("X Wins!")
            break
        turn = not turn
        if counter == 9:
            print ("Tie!")
    
tictactoe()
