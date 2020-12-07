from random import randrange
import time

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(len(board)):
        print("+---+---+---+")
        for j in range(len(board[i])):
            print("|",board[i][j],end=" ")
        print("|")
    print("+---+---+---+")
    time.sleep(1)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    li = [1,2,3,4,5,6,7,8,9]
    freeli=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in li:
               freeli += [(i,j)]
    print("hey, list of free fields: ",freeli)
    return freeli

def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.
    u_move = int(input("enter a number between 1 and 9: "))
    if u_move not in li:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if u_move == board[i][j]:
                    if (i,j) in make_list_of_free_fields(board):
                        board[i][j] = 'O'
                        break
        li.append(u_move)
        print("list is",li)
    else:
        print(u_move,"is not free,try another move")
        enter_move(board)
    return board

def victory_for(board):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    xcount=0
    ocount=0
    #check row 0
    if board[0][0] == board[0][1] == board[0][2] == 'X':
        xcount += 1
    elif board[0][0] == board[0][1] == board[0][2] == 'O':
        ocount += 1
    #check row 1
    if board[1][0] == board[1][1] == board[1][2] == 'X':
        xcount += 1
    elif board[1][0] == board[1][1] == board[1][2] == 'O':
        ocount += 1
    #check row 2
    if board[2][0] == board[2][1] == board[2][2] == 'X':
        xcount += 1
    elif board[2][0] == board[2][1] == board[2][2] == 'O':
        ocount += 1
    #check column 0
    if board[0][0] == board[1][0] == board[2][0] == 'X':
        xcount += 1
    elif board[0][0] == board[1][0] == board[2][0] == 'O':
        ocount += 1
    #check column 1
    if board[0][1] == board[1][1] == board[2][1] == 'X':
        xcount += 1
    elif board[0][1] == board[1][1] == board[2][1] == 'O':
        ocount += 1
    #check column 2
    if board[0][2] == board[1][2] == board[2][2] == 'X':
        xcount += 1
    elif board[0][2] == board[1][2] == board[2][2] == 'O':
        ocount += 1
    #check diagonal top left
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        xcount += 1
    elif board[0][0] == board[1][1] == board[2][2] == 'O':
        ocount += 1
    #check diagonal bottom left
    if board[2][0] == board[1][1] == board[0][2] == 'X':
        xcount += 1
    elif board[2][0] == board[1][1] == board[0][2] == 'O':
        ocount += 1

    if xcount > ocount :
      print("'X' won the game")
    elif xcount < ocount:
      print("'O' won the game")
    else:
      print("it is a tie or neither 'X' nor 'O' won the game")


def draw_move(board):
    c_move = randrange(1,10)
    print("random number is: ",c_move)
    if c_move not in li:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == c_move:
                    if (i,j) in make_list_of_free_fields(board):
                        board[i][j] = 'X'
                        break
        li.append(c_move)
        print("list is",li)
    else:
        print(c_move,"is not free,try another move")
        draw_move(board)
    return board

board = [[1,2,3],
         [4,'X',6],
         [7,8,9]]

li = [5]
print(display_board(board))

for i in range(8):
    if i%2 == 0:
        print(i)
        board=enter_move(board)
        display_board(board)
    else:
        print(i)
        board=draw_move(board)
        display_board(board)
else:
    victory_for(board)
