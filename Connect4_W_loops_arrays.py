player1Wins = 0
player2Wins = 0
totalPlayer1Wins = 0
totalPlayer2Wins = 0

import random

scoreboard = player1Wins , player2Wins



print("Hello, and welcome to Connect 4! what is Player 1's name?")
player1 = input()

print(f"Great to meet you {player1}!")
print("How many humans are competeing?")
gamemode = input()


if gamemode == "2":
     print("who is Player2? \n")
     player2 = input()
else:
    player2 = "CPU"
print(f"Great, now lets begin!")
print("You will Press the number key associated with your desired spot to play your turn")


play_again = True

while play_again:

    total_board = totalPlayer1Wins, totalPlayer2Wins

    print("The current score is ", total_board)


    player1Wins = 0
    player2Wins = 0


    while player1Wins < 2 and player2Wins < 2:
        winner = False
        token = "(-O)"

        print_board = [
            "[0] ", "[1]", " [2] ", "[3] ", "[4]", "[5] ", " [6] ",
            "[7] ", "[8] ", "[9] ", "[10]", "[11]", "[12]", "[13]",
            "[14]", "[15]", "[16]", "[17]", "[18]", "[19]", "[20]",
            "[21]", "[22]", "[23]", "[24]", "[25]", "[26]", "[27]",
            "[28]", "[29]", "[30]", "[31]", "[32]", "[33]", "[34]",
            "[35]", "[36]", "[37]", "[38]", "[39]", "[40]", "[41]"
        ]
        def printboard(print_board):
                print(print_board[0], print_board[1], print_board[2], print_board[3], print_board[4], print_board[5], print_board[6])
                print(print_board[7], print_board[8], print_board[9], print_board[10], print_board[11], print_board[12], print_board[13])
                print(print_board[14], print_board[15], print_board[16], print_board[17], print_board[18], print_board[19], print_board[20])
                print(print_board[21], print_board[22], print_board[23], print_board[24], print_board[25], print_board[26], print_board[27])
                print(print_board[28], print_board[29], print_board[30], print_board[31], print_board[32], print_board[33], print_board[34])
                print(print_board[35], print_board[36], print_board[37], print_board[38], print_board[39], print_board[40], print_board[41])
        
        for turn in range(42):
            if token == "(-O)":
                token = "(-X)"
            else:
                token = "(-O)"

            printboard(print_board)

            if gamemode != "2" and token == "(-O)":
                print("\n\n")
                availableCells = []

                for i in range(7):
                    availableCells.append(i)

                slot = random.choice(availableCells)
            else:
                print("Choose a slot, slots are chosen with numbers 0, 1, 2, 3, 4, 5, 6")
                slot = int(input("slot: "))

            for row in range(5, -1, -1):
                position = slot + (row * 7)

                if print_board[position].strip("[] ") == str(position):
                    print_board[position] = token
                    break


        totalPlayer1Wins += player1Wins
        totalPlayer2Wins += player2Wins        
        print("Would you like to play again? (yes/no)")
        answer = input().lower()
        
        if answer == "no" or answer == "n" or answer == "No" or answer == "N" or answer == "Nah" or answer == "nah" or answer == "go to hell":
            play_again = False
        
        print(f"\n Thank you, \n \tI hope you have enjoyed your time \n{player1} \n and \n {player2} \n Have a wonderful day!")

        
        


