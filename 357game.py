# I import the directory "time" to allow for the
# game to pause before executing more lines of code
import time
import random
import math

#above are different directories which have functions already defined inside them

BoardValue = (7,5,3)

# This is every possible number of blocks available for each row
A7 = "A [] [] [] [] [] [] []"
A6 = "A [] [] [] [] [] []"
A5 = "A    [] [] [] [] []"
A4 = "A    [] [] [] []"
A3 = "A       [] [] []"
A2 = "A       [] []"
A1 = "A          []"
A0 = "A"
B5 = "B    [] [] [] [] []"
B4 = "B    [] [] [] []"
B3 = "B       [] [] []"
B2 = "B       [] []"
B1 = "B          []"
B0 = "B"
C3 = "C       [] [] []"
C2 = "C       [] []"
C1 = "C          []"
C0 = "C"

# This is a function that will print out the starting board
def StartingBoard():
    print(A7)
    print("")
    print(B5)
    print("")
    print(C3)
    print("")

# This defines the function that will print out the instructions and an example    
def Rules():
    print('')
    print("The game is called 3-5-7")
    print("The goal of the game is to make your opponent pick the last block")
    print("The board looks like this -")
    print("")
    time.sleep(1)
    StartingBoard()
    time.sleep(4)
    print("The player who starts gets to choose one row (A, B, or C)")
    print("then chooses an amount to take from that row.")
    time.sleep(2)
    print("")
    print("After one player goes the next player then chooses his row, and ")
    print("how many blocks he wishes to take from that row")
    print("")
    time.sleep(2)
    print("Here is an example-")
    time.sleep(2)
    print("")
    StartingBoard()
    time.sleep(2)
    print("Player 1 chooses to take 4 blocks from row A")
    time.sleep(2)
    print("")
    print(A3)
    print("")
    print(B5)
    print("")
    print(C3)
    print("")
    time.sleep(2)
    print("Now player 2 chooses to take 5 blocks from row B")
    time.sleep(2)
    print("")
    print(A3)
    print("")
    print(B0)
    print("")
    print(C3)
    time.sleep(2)
    print("")
    print("Player 1 now takes 3 blocks from row C")
    time.sleep(2)
    print("")
    print(A3)
    print("")
    print(B0)
    print("")
    print(C0)
    time.sleep(2)
    print("")
    print("Now player 2 takes 2 blocks from row A")
    time.sleep(2)
    print("")
    print(A1)
    print("")
    print("B")
    print("")
    print("C")
    print("")
    time.sleep(2)
    print("Player 1 takes the last block from row A")
    time.sleep(2)
    print('')
    print(A0)
    print("")
    print(B0)
    print("")
    print("C")
    print("")
    time.sleep(2)
    print("Player 2 wins!")
    time.sleep(2)
    print("Player 1 was forced to draw the last block so now player 2 is the winner")
    print('')

# This function asks if you want to hear the rules or not
def RulesPrompt():
    print("Would you like to hear the rules?")
    answer = input("Yes or No ")
    if answer == "Yes" or answer == "y" or answer == "yes" or answer == "Y" or answer == "YES":
        Rules()
    elif answer == "No" or answer == "n" or answer == "no" or answer == "NO" or answer == "N":
        print("Sounds good!")
    else:
        print("invalid input")
        time.sleep(2)
        RulesPrompt()

# This is a function for the computer's move choice


def ComputerMove():
    global BoardValue
    # The global keyword brings the global variable "BoardValue" into the function
    
    if BoardValue == (7,5,3):
        FirstMove = random.randint(1,3)
        if FirstMove == 1:
            BoardValue = (6,5,3)
        elif FirstMove == 2:
            BoardValue = (7,4,3)
        elif FirstMove == 3:
            BoardValue = (7,5,2)
    elif BoardValue == (0,0,1):
        BoardValue = (0,0,0)
    elif BoardValue == (0,0,2):
        BoardValue = (0,0,1)
    elif BoardValue == (0,0,3):
        BoardValue = (0,0,1)
    elif BoardValue == (0,1,0):
        BoardValue = (0,0,0)
    elif BoardValue == (0,1,1):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (0,0,1)
        elif choice == 2:
            BoardValue = (0,1,0)
    elif BoardValue == (0,1,2):
        BoardValue = (0,1,0)
    elif BoardValue == (0,1,3):
        BoardValue = (0,1,0)
    elif BoardValue == (0,2,0):
        BoardValue = (0,1,0)
    elif BoardValue == (0,2,1):
        BoardValue = (0,0,1)
    elif BoardValue == (0,2,2):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (0,1,2)
        elif choice == 2:
            BoardValue = (0,2,1)
    elif BoardValue == (0,2,3):
        BoardValue = (0,2,2)
    elif BoardValue == (0,3,0):
        BoardValue = (0,1,0)
    elif BoardValue == (0,3,1):
        BoardValue = (0,0,1)
    elif BoardValue == (0,3,2):
        BoardValue = (0,2,2)
    elif BoardValue == (0,3,3):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (0,3,2)
        elif choice == 2:
            BoardValue = (0,2,3)
    elif BoardValue == (0,4,0):
        BoardValue = (0,1,0)
    elif BoardValue == (0,4,1):
        BoardValue = (0,0,1)
    elif BoardValue == (0,4,2):
        BoardValue = (0,2,2)
    elif BoardValue == (0,4,3):
        BoardValue = (0,3,3)
    elif BoardValue == (0,5,0):
        BoardValue = (0,1,0)
    elif BoardValue == (0,5,1):
        BoardValue = (0,0,1)
    elif BoardValue == (0,5,2):
        BoardValue = (0,2,2)
    elif BoardValue == (0,5,3):
        BoardValue = (0,3,3)
    elif BoardValue == (1,0,0):
        BoardValue = (0,0,0)
    elif BoardValue == (1,0,1):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (1,0,0)
        elif choice == 2:
            BoardValue = (0,0,1)
    elif BoardValue == (1,0,2):
        BoardValue = (1,0,0)
    elif BoardValue == (1,0,3):
        BoardValue = (1,0,0)
    elif BoardValue == (1,1,0):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (1,0,0)
        elif choice == 2:
            BoardValue = (0,1,0)
    elif BoardValue == (1,1,1):
        choice = random.randint(1,3)
        if choice == 1:
            BoardValue = (1,1,0)
        elif choice == 2:
            BoardValue = (1,0,1)
        elif choice == 3:
            BoardValue = (0,1,1)
    elif BoardValue == (1,1,2):
        BoardValue = (1,1,1)
    elif BoardValue == (1,1,3):
        BoardValue = (1,1,1)
    elif BoardValue == (1,2,0):
        BoardValue = (1,0,0)
    elif BoardValue == (1,2,1):
        BoardValue = (1,1,1)
    elif BoardValue == (1,2,2):
        BoardValue = (0,2,2)
    elif BoardValue == (1,2,3):
        BoardValue = (1,1,3)
    elif BoardValue == (1,3,0):
        BoardValue = (1,0,0)
    elif BoardValue == (1,3,1):
        BoardValue = (1,1,1)
    elif BoardValue == (1,3,2):
        BoardValue = (1,3,1)
    elif BoardValue == (1,3,3):
        BoardValue = (0,3,3)
    elif BoardValue == (1,4,0):
        BoardValue = (1,0,0)
    elif BoardValue == (1,4,1):
        BoardValue = (1,1,1)
    elif BoardValue == (1,4,2):
        BoardValue = (1,3,2)
    elif BoardValue == (1,4,3):
        BoardValue = (1,2,3)
    elif BoardValue == (1,5,0):
        BoardValue = (1,0,0)
    elif BoardValue == (1,5,1):
        BoardValue = (1,1,1)
    elif BoardValue == (1,5,2):
        BoardValue = (1,3,2)
    elif BoardValue == (1,5,3):
        BoardValue = (1,2,3)
    elif BoardValue == (2,0,0):
        BoardValue =  (1,0,0)
    elif BoardValue == (2,0,1):
        BoardValue = (0,0,1)
    elif BoardValue == (2,0,2):
        BoardValue = (1,0,2)
    elif BoardValue == (2,0,3):
        BoardValue = (2,0,2)
    elif BoardValue == (2,1,0):
        BoardValue = (0,1,0)
    elif BoardValue == (2,1,1):
        BoardValue = (1,1,1)
    elif BoardValue == (2,1,2):
        BoardValue = (2,0,2)
    elif BoardValue == (2,1,3):
        BoardValue = (1,1,3)
    elif BoardValue == (2,2,0):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (1,2,0)
        elif choice == 2:
            BoardValue = (2,1,0)
    elif BoardValue == (2,2,1):
        BoardValue = (2,2,0)
    elif BoardValue == (2,2,2):
        choice = random.randint(1,3)
        if choice == 1:
            BoardValue = (0,2,2)
        elif choice == 2:
            BoardValue = (2,0,2)
        elif choice == 3:
            BoardValue = (2,2,0)
    elif BoardValue == (2,2,3):
        BoardValue = (2,2,0)
    elif BoardValue == (2,3,0):
        BoardValue = (2,2,0)
    elif BoardValue == (2,3,1):
        BoardValue = (1,3,1)
    elif BoardValue == (2,3,2):
        BoardValue = (2,0,2)
    elif BoardValue == (2,3,3):
        BoardValue = (0,3,3)
    elif BoardValue == (2,4,0):
        BoardValue = (2,2,0)
    elif BoardValue == (2,4,1):
        BoardValue = (2,3,1)
    elif BoardValue == (2,4,2):
        BoardValue = (2,0,2)
    elif BoardValue == (2,4,3):
        BoardValue = (2,1,3)
    elif BoardValue == (2,5,0):
        BoardValue = (2,2,0)
    elif BoardValue == (2,5,1):
        BoardValue = (2,3,1)
    elif BoardValue == (2,5,2):
        BoardValue = (2,0,2)
    elif BoardValue == (2,5,3):
        BoardValue = (2,1,3)
    elif BoardValue == (3,0,0):
        BoardValue = (1,0,0)
    elif BoardValue == (3,0,1):
        BoardValue = (0,0,1)
    elif BoardValue == (3,0,2):
        BoardValue = (2,0,2)
    elif BoardValue == (3,0,3):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (2,0,3)
        elif choice == 2:
            BoardValue = (3,0,2)
    elif BoardValue == (3,1,0):
        BoardValue = (0,1,0)
    elif BoardValue == (3,1,1):
        BoardValue = (1,1,1)
    elif BoardValue == (3,1,2):
        BoardValue = (3,1,1)
    elif BoardValue == (3,1,3):
        BoardValue = (3,0,3)
    elif BoardValue == (3,2,0):
        BoardValue = (2,2,0)
    elif BoardValue == (3,2,1):
        BoardValue = (3,1,1)
    elif BoardValue == (3,2,2):
        BoardValue = (0,2,2)
    elif BoardValue == (3,2,3):
        BoardValue = (3,2,1)
    elif BoardValue == (3,3,0):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (2,3,0)
        elif choice == 2:
            BoardValue = (3,2,0)
    elif BoardValue == (3,3,1):
        BoardValue = (3,3,0)
    elif BoardValue == (3,3,2):
        BoardValue = (3,3,0)
    elif BoardValue == (3,3,3):
        choice = random.randint(1,3)
        if choice == 1:
            BoardValue = (0,3,3)
        elif choice == 2:
            BoardValue = (3,0,3)
        elif choice ==3:
            BoardValue = (3,3,0)
    elif BoardValue == (3,4,0):
        BoardValue = (3,3,0)
    elif BoardValue == (3,4,1):
        BoardValue = (3,2,1)
    elif BoardValue == (3,4,2):
        BoardValue = (3,1,2)
    elif BoardValue == (3,4,3):
        BoardValue = (3,0,3)
    elif BoardValue == (3,5,0):
        BoardValue = (3,3,0)
    elif BoardValue == (3,5,1):
        BoardValue = (3,2,1)
    elif BoardValue == (3,5,2):
        BoardValue = (3,1,2)
    elif BoardValue == (3,5,3):
        BoardValue = (3,0,3)
    elif BoardValue == (4,0,0):
        BoardValue = (1,0,0)
    elif BoardValue == (4,0,1):
        BoardValue = (0,0,1)
    elif BoardValue == (4,0,2):
        BoardValue = (2,0,2)
    elif BoardValue == (4,0,3):
        BoardValue = (3,0,3)
    elif BoardValue == (4,1,0):
        BoardValue = (0,1,0)
    elif BoardValue == (4,1,1):
        BoardValue = (1,1,1)
    elif BoardValue == (4,1,2):
        BoardValue = (3,1,2)
    elif BoardValue == (4,1,3):
        BoardValue = (2,1,3)
    elif BoardValue == (4,2,0):
        BoardValue = (2,2,0)
    elif BoardValue == (4,2,1):
        BoardValue = (3,2,1)
    elif BoardValue == (4,2,2):
        BoardValue = (0,2,2)
    elif BoardValue == (4,2,3):
        BoardValue = (1,2,3)
    elif BoardValue == (4,3,0):
        BoardValue = (3,3,0)
    elif BoardValue == (4,3,1):
        BoardValue = (2,3,1)
    elif BoardValue == (4,3,2):
        BoardValue = (1,3,2)
    elif BoardValue == (4,3,3):
        BoardVale = (0,3,3)
    elif BoardValue == (4,4,0):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (3,4,0)
        elif choice == 2:
            BoardValue = (4,3,0)
    elif BoardValue == (4,4,1):
        BoardValue = (4,4,0)
    elif BoardValue == (4,4,2):
        BoardValue = (4,4,0)
    elif BoardValue == (4,4,3):
        BoardValue = (4,4,0)
    elif BoardValue == (4,5,0):
        BoardValue = (4,4,0)
    elif BoardValue == (4,5,1):
        BoardValue = (4,3,1)
    elif BoardValue == (4,5,2):
        BoardValue = (4,5,1)
    elif BoardValue == (4,5,3):
        BoardValue = (4,5,1)
    elif BoardValue == (5,0,0):
        BoardValue = (1,0,0)
    elif BoardValue == (5,0,1):
        BoardValue = (0,0,1)
    elif BoardValue == (5,0,2):
        BoardValue = (2,0,2)
    elif BoardValue == (5,0,3):
        BoardValue = (3,0,3)
    elif BoardValue == (5,1,0):
        BoardValue = (0,1,0)
    elif BoardValue == (5,1,1):
        BoardValue = (1,1,1)
    elif BoardValue == (5,1,2):
        BoardValue = (3,1,2)
    elif BoardValue == (5,1,3):
        BoardValue = (2,1,3)
    elif BoardValue == (5,2,0):
        BoardValue = (2,2,0)
    elif BoardValue == (5,2,1):
        BoardValue = (3,2,1)
    elif BoardValue == (5,2,2):
        BoardValue = (0,2,2)
    elif BoardValue == (5,2,3):
        BoardValue = (1,2,3)
    elif BoardValue == (5,3,0):
        BoardValue = (3,3,0)
    elif BoardValue == (5,3,1):
        BoardValue = (2,3,1)
    elif BoardValue == (5,3,2):
        BoardValue = (1,3,2)
    elif BoardValue == (5,3,3):
        BoardValue = (0,3,3)
    elif BoardValue == (5,4,0):
        BoardValue = (4,4,0)
    elif BoardValue == (5,4,1):
        BoardValue = (3,4,1)
    elif BoardValue == (5,4,2):
        BoardValue = (5,4,1)
    elif BoardValue == (5,4,3):
        BoardValue = (5,4,1)
    elif BoardValue == (5,5,0):
        choice = random.randint(1,2)
        if choice == 1:
            BoardValue = (4,5,0)
        elif choice == 2:
            BoardValue = (5,4,0)
    elif BoardValue == (5,5,1):
        BoardValue = (5,5,0)
    elif BoardValue == (5,5,2):
        BoardValue = (5,5,0)
    elif BoardValue == (5,5,3):
        BoardValue = (5,5,0)
    elif BoardValue == (6,0,0):
        BoardValue = (1,0,0)
    elif BoardValue == (6,0,1):
        BoardValue = (0,0,1)
    elif BoardValue == (6,0,2):
        BoardValue = (2,0,2)
    elif BoardValue == (6,0,3):
        BoardValue = (3,0,3)
    elif BoardValue == (6,1,0):
        BoardValue = (0,1,0)
    elif BoardValue == (6,1,1):
        BoardValue = (1,1,1)
    elif BoardValue == (6,1,2):
        BoardValue = (3,1,2)
    elif BoardValue == (6,1,3):
        BoardValue = (2,1,3)
    elif BoardValue == (6,2,0):
        BoardValue = (2,2,0)
    elif BoardValue == (6,2,1):
        BoardValue = (3,2,1)
    elif BoardValue == (6,2,2):
        BoardValue = (0,2,2)
    elif BoardValue == (6,2,3):
        BoardValue = (1,2,3)
    elif BoardValue == (6,3,0):
        BoardValue = (3,3,0)
    elif BoardValue == (6,3,1):
        BoardValue = (2,3,1)
    elif BoardValue == (6,3,2):
        BoardValue = (1,3,2)
    elif BoardValue == (6,3,3):
        BoardValue = (0,3,3)
    elif BoardValue == (6,4,0):
        BoardValue = (4,4,0)
    elif BoardValue == (6,4,1):
        BoardValue = (5,4,1)
    elif BoardValue == (6,4,2):
        BoardValue = (5,4,2)
    elif BoardValue == (6,4,3):
        BoardValue = (6,4,2)
    elif BoardValue == (6,5,0):
        BoardValue = (5,5,0)
    elif BoardValue == (6,5,1):
        BoardValue = (4,5,1)
    elif BoardValue == (6,5,2):
        BoardValue = (6,4,2)
    elif BoardValue == (6,5,3):
        BoardValue = (6,5,1)
    elif BoardValue == (6,5,2):
        BoardValue = (6,4,2)
    elif BoardValue == (6,5,3):
        BoardValue = (6,5,1)
    elif BoardValue == (7,0,0):
        BoardValue = (1,0,0)
    elif BoardValue == (7,0,1):
        BoardValue = (0,0,1)
    elif BoardValue == (7,0,2):
        BoardValue = (2,0,2)
    elif BoardValue == (7,0,3):
        BoardValue = (3,0,3)
    elif BoardValue == (7,1,0):
        BoardValue = (0,1,0)
    elif BoardValue == (7,1,1):
        BoardValue = (1,1,1)
    elif BoardValue == (7,1,2):
        BoardValue = (3,1,2)
    elif BoardValue == (7,1,3):
        BoardValue = (2,1,3)
    elif BoardValue == (7,2,0):
        BoardValue = (2,2,0)
    elif BoardValue == (7,2,1):
        BoardValue = (3,2,1)
    elif BoardValue == (7,2,2):
        BoardValue = (0,2,2)
    elif BoardValue == (7,2,3):
        BoardValue = (1,2,3)
    elif BoardValue == (7,3,0):
        BoardValue = (3,3,0)
    elif BoardValue == (7,3,1):
        BoardValue = (2,3,1)
    elif BoardValue == (7,3,2):
        BoardValue = (1,3,2)
    elif BoardValue == (7,3,3):
        BoardValue = (0,3,3)
    elif BoardValue == (7,4,0):
        BoardValue = (4,4,0)
    elif BoardValue == (7,4,1):
        BoardValue = (5,4,1)
    elif BoardValue == (7,4,2):
        BoardValue = (6,4,2)
    elif BoardValue == (7,4,3):
        BoardValue = (5,4,3)
    elif BoardValue == (7,5,0):
        BoardValue = (5,5,0)
    elif BoardValue == (7,5,1):
        BoardValue = (4,5,1)
    elif BoardValue == (7,5,2):
        BoardValue = (4,5,2)
# I finished!!!!!
# That was every single board combination and what move the computer should make for each one

# and this is the funciton for the player's move
def PlayerMove():
    global BoardValue
    row = str(input("Choose a row (A,B, or C) "))
    while len(row) > 1 or row == '':
        print ('''Invalid input
Try again''')
        row = str(input("Choose a row (A,B, or C) "))
        if len(row) == 1:
            break
        print("")
    amount = input("How many? ")
    while amount == '0' or (amount != '1' and amount != '2' and amount != '3' and amount != '4' and amount != '5' and amount != '6' and amount != '7'):
        print("Invalid inut ")
        print (amount)
        amount = input("How many? ")
        if amount == '1' or amount =='2' or amount == '3' or amount == '4' or amount == '5' or amount == '6' or amount == '7':
            break
# the bit above was a bit difficult to figure out because it kept returning as invalid input when the input was valid
# but I eventually figured it out
    while amount == ('') and (row == ('a') or row == ('b') or row == ('c') or row == ('A') or row == ("C") or row == ("B")):
        print("invalid input")
        amount = input("How many? ")
    if row == "a" or row == "A":
        if BoardValue[0] - abs(int(amount)) >= 0:
            BoardValue = (BoardValue[0] - abs(int(amount)), BoardValue[1], BoardValue[2])
        else:
            print("Invalid Input")
            print('')
            print("Try again")
            PlayerMove()
    elif row == "b" or row == "B":
        if BoardValue[1] - abs(int(amount)) >= 0:
            BoardValue = (BoardValue[0], BoardValue[1] - abs(int(amount)), BoardValue[2])
        else:
            print("Invalid Input")
            print("")
            print("Try again")
            PlayerMove()
    elif row == "c" or row == "C":
        if BoardValue[2] - abs(int(amount)) >= 0:
            BoardValue = (BoardValue[0], BoardValue[1], BoardValue[2] - abs(int(amount)))
        else:
            print("Invalid Input")
            print('')
            print("Try again")
            PlayerMove()
    else:
        print("Invalid Input")
        print("")
        print("Try again")
        PlayerMove()
    

# this function prints the board
def BoardPrint():

    def rowA():
        global BoardValue
        global A7
        global A6
        global A5
        global A4
        global A3
        global A2
        global A1
        global A0

        if BoardValue[0] == 7:
            print(A7)
        elif BoardValue[0] == 6:
            print(A6)
        elif BoardValue[0] == 5:
            print(A5)
        elif BoardValue[0] == 4:
            print(A4)
        elif BoardValue[0] == 3:
            print(A3)
        elif BoardValue[0] == 2:
            print(A2)
        elif BoardValue[0] == 1:
            print(A1)
        elif BoardValue[0] == 0:
            print(A0)
        else:
            print("Something went wrong")
            
    def rowB():
        global BoardValue
        global B5
        global B4
        global B3
        global B2
        global B1
        global B0

        if BoardValue[1] == 5:
            print(B5)
        elif BoardValue[1] == 4:
            print(B4)
        elif BoardValue[1] == 3:
            print(B3)
        elif BoardValue[1] == 2:
            print(B2)
        elif BoardValue[1] == 1:
            print(B1)
        elif BoardValue[1] == 0:
            print(B0)
        else:
            print("Something went wrong")

    def rowC():
        global BoardValue
        global C3
        global C2
        global C1
        global C0

        if BoardValue[2] == 3:
            print(C3)
        elif BoardValue[2] == 2:
            print(C2)
        elif BoardValue[2] == 1:
            print(C1)
        elif BoardValue[2] == 0:
            print(C0)
        else:
            print("Something went wrong")
    print(BoardValue)
    rowA()
    print("")
    rowB()
    print("")
    rowC()
#This function is for a player vs. player game
def PvP():
    Player1 = input("Player 1 enter a name --> ")
    Player2 = input("Player 2 enter a name --> ")
    while BoardValue != (0,0,0):
        if BoardValue != (0,0,0):
            print("")
            print(Player1 + "'s turn")
            BoardPrint()
            PlayerMove()
        if BoardValue == (0,0,0):
            print("")
            print(Player2 + " wins!")
            break
        if BoardValue != (0,0,0):
            print("")
            print(Player2 + "'s turn")
            BoardPrint()
            PlayerMove()
        else:
            print("")
            print(Player2 + " wins!")
            break
        if BoardValue == (0,0,0):
            print("")
            print(Player1 + " wins!")
            break
#This function is used to decide if the player goes first or second when playing against a computer
def move():
    moveChoice = ''
    while moveChoice != '1' and moveChoice != '2' and moveChoice != 'first' and moveChoice != 'second' and moveChoice != 'First' and moveChoice != 'Second' and moveChoice != 'FIRST' and moveChoice != 'SECOND':
        print('Do you want to go first or second? (1 or 2)')
        moveChoice = input()
    if moveChoice == '1' or moveChoice == 'first':
        PvC('1')
    elif moveChoice == '2' or moveChoice == 'second':
        PvC('2')

# this function is used when playing against the computer
def PvC(order):
    if order == "1" or order == "first" or order == "First":
        while BoardValue != (0,0,0):
            if BoardValue != (0,0,0):
                print('')
                print('Your turn')
                BoardPrint()
                PlayerMove()
                BoardPrint()
            if BoardValue == (0,0,0):
                print('')
                time.sleep(2)
                print('You lose')
                break
            print('')
            time.sleep(2)
            print('My turn')
            time.sleep(2)
            ComputerMove()
            print('')
            time.sleep(2)
            if BoardValue == (0,0,0):
                print('')
                time.sleep(2)
                BoardPrint()
                print('You won!!!')
                break
    elif order == "2" or order == "second" or order == "Second":
        while BoardValue != (0,0,0):
            if BoardValue != (0,0,0):
                print('')
                BoardPrint()
                print('')
                time.sleep(2)
                print('My turn')
                ComputerMove()
                print('')
                time.sleep(2)
                if BoardValue == (0,0,0):
                    print('')
                    time.sleep(2)
                    BoardPirnt()
                    print('You won!!!')
                    break
            print('')
            time.sleep(2)
            print('Your turn')
            BoardPrint()
            PlayerMove()
            if BoardValue == (0,0,0):
                print('')
                time.sleep(2)
                BoardPrint()
                print('You lose')
                break
            
#this is a funcion for choosing if you want to play against the computer or another player
def GameMode():
    print('Choose your game mode')
    print('')
    print('1 - Player vs. Computer')
    print('or')
    print('2 - Player vs. Player')
    gameChoice = input('1 or 2  ')
    if gameChoice == '1':
        move()
    elif gameChoice == '2':
        PvP()
    elif gameChoice == '':
        print("invalid input")
        GameMode()
    else:
        print("Invalid input")
        GameMode()

# This is where all the code above is actually executed
# Without it the program wouldn't run
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    RulesPrompt()
    BoardValue = (7,5,3)
    GameMode()
    print('Do you want to play again (yes or no)')
    playAgain = input()