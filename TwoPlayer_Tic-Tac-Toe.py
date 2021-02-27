#Two Player Tic-Tac-Toe game in Python.

#create a blank board
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

#get all the key form board directory
board_keys = []
for key in theBoard:
    board_keys.append(key)

#print board directory
def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+--+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+--+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    choice = getUserChoice()
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + choice + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = choice
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        
        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                gameOver(choice)                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                gameOver(choice)
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                gameOver(choice)
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                gameOver(choice)
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                gameOver(choice)
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                gameOver(choice)
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                gameOver(choice)
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                gameOver(choice)
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            gameOver()

        # Now we have to change the player after every move.
        if choice =='X':
            choice = 'O'
        else:
            choice = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart.lower == "y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

def getUserChoice():
    choice=False
    while choice == False:
        userInput = input('Player 1 input your choice X or O : ')
        if(userInput.lower() == 'x' or userInput.lower() == 'o'):
            choice = True
            return userInput.upper()
        else:
            choice=False
            print('Please enter a valid choice to start the game.')

def gameOver(msgType):
    
    print("\nGame Over.\n")   
    if(msgType.lower == 'x' or msgType.lower == 'o'):
        print(" **** Congratulation! Winner is " + msgType + ". ****")
    else:
        print(" **** It's a Tie between both the players!! ****")

#Let's start the game
game()
