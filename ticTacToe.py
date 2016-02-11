def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or
        (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or
        (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or
        (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or
        (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player)or
        (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or
        (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or
        (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player)) 
    
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer # asking for the starting player 
    for i in range(9):    # it is going through the 9 spot's on the board
        printBoard(board)  # call the print board function and passes baord
        print('Turn for ' + turn + '. Move on which space?')    # asking the player to choose a space  
        move = input()       # player chooses the position on the board
        board[move] = turn    # set's the position 
        if( checkWinner(board, 'X') ):   # if the player X has 3 winning position on the board 
            print('X wins!')            # prints the player X wins 
            break                       # breaking out of the if function
        elif ( checkWinner(board, 'O') ): # if the player O has 3 winning position on the board 
            print('O wins!')              # prints the player O wins 
            break                       # breaking out of the if function
    
        if turn == 'X':                 # if it's X's turn 
            turn = 'O'                  # switch to O 
        else:
            turn = 'X'                  # it's X's turn
        
    printBoard(board)                   # print the board with a new selection
