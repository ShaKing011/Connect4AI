# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Step 1 : board representation
# Step 2 : board print to command line
# Step 3 : get move + makes mo  `ves + alternate players
# Step 4 : win check
# Step 5 : AI

player1 = 1 #to be X
player2 = -1 #to be O
board = [ [0,0,0,0,0,0,0], [0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0] ,[0,0,0,0,0,0,0] ]



def printboard( board ):
    for rows in range(6):
        for column in range(7):
            if board[rows][column] == 0:
                print("_" , end = " | ")
            if board[rows][column] == 1:
                print("X", end = " | ")
            if board[rows][column] == -1:
                print("O", end = " | ")
        print("")

def getmove():
    move = input("input column number between 1 and 7 ")
    move = int(move)
    while not validCheck(board , move-1):
        move = input("input column number between 1 and 7 ")
        move = int(move)

    return move-1

def validCheck( board , move ):
    spaceCheck = 0
    if move > 6 or move < 0:
        return False
    for i in range(5,-1,-1):
        if board[i][move] == 0:
            spaceCheck +=1
    if spaceCheck == 0:
        return False
    else:
        return True


def makemove( move , player):
    for i in range(5,-1,-1):
        if board[i][move] == 0:
            board[i][move] = player
            return


def wincheck( board ):
    #Check horizontal
    for i in range(6):
        for j in range(4):
            if board[i][j] == 1 and board[i][j+1] == 1 and board[i][j+2] == 1 and board[i][j+3] == 1:
                return 10
            elif board[i][j] == -1 and board[i][j+1] == -1 and board[i][j+2] == -1 and board[i][j+3] == -1:
                return -10
    #Check Verticcal
    for j in range(7):
        for i in range(3):
            if board[i][j] == 1 and board[i+1][j] == 1 and board[i+2][j] == 1 and board[i+3][j] == 1:
                return 10
            elif board[i][j] == -1 and board[i+1][j] == -1 and board[i+2][j] == -1 and board[i+3][j] == -1:
                return -10
    #Check rising diagnal
    for i in range(3,6):
        for j in range(4):
            if board[i][j] == 1 and board[i-1][j+1] == 1 and board[i-2][j+2] == 1 and board[i-3][j+3] == 1:
                return 10
            elif board[i][j] == -1 and board[i-1][j+1] == -1 and board[i-2][j+2] == -1 and board[i-3][j+3] == -1:
                return -10
    #Check falling diagnal
    for i in range(2,-1,-1):
        for j in range(4):
            if board[i][j] == 1 and board[i+1][j+1] == 1 and board[i+2][j+2] == 1 and board[i+3][j+3] == 1:
                return 10
            elif board[i][j] == -1 and board[i+1][j+1] == -1 and board[i+2][j+2] == -1 and board[i+3][j+3] == -1:
                return -10
    drawCount = 0
    for i in range(6):
        for j in range(7):
            if board[i][j] != 0:
                drawCount += 1
    if drawCount == 42:
        return 0

    return (-1)

#AI Generation functions
def makemoveAI( move , player):
    for i in range(5,-1,-1):
        if board[i][move] == 0:
            board[i][move] = player
            return i


def availMoves( board ):
    availColumns = []
    for col in range(7):
        for row in range(5,-1,-1):
            if board[row][col] == 0:
                availColumns.append(col)
                break

    return availColumns


def findbestmove(board , player):
    bestval = -100
    bestMove = 0
    for moves in availMoves(board):
        i = makemoveAI(moves , player)
        moveEval = minimax( board, 1 , 4 )
        board[i][moves] = 0
        if moveEval > bestval:
            bestval = moveEval
            bestMove = moves

    return bestMove

def minimax(board, player, depth):
    if wincheck(board) == 10:
        return -10
    elif wincheck(board) == -10:
        return 10
    elif wincheck(board) == 0:
        return 0
    if depth == 0:
        return 0

    if player == -1:
        best = -100000
        for moves in availMoves(board):
            i = makemoveAI(moves, player)
            best = max( best, minimax(board, -player, depth - 1) )
            board[i][moves] = 0
        return best

    else:
        best = 100000
        for moves in availMoves(board):
            i = makemoveAI(moves, player)
            best = min(best, minimax(board, -player, depth - 1) )
            board[i][moves] = 0
        return best





gamer = 1
while wincheck(board) ==  -1:
    printboard(board)
    print(" ")

    if gamer == 1:
        m = getmove()
        makemove(m, gamer)
        gamer = -gamer
    else:
        AImove = findbestmove(board , -1)
        makemove(AImove, gamer)
        gamer= -gamer



if wincheck(board) == 10:
    printboard(board)
    print("player1 wins!")
elif wincheck(board) == -10:
    printboard(board)
    print("player2 wins!")
elif wincheck(board) == 0:
    printboard(board)
    print("Draw!")

