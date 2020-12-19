def drawBoard(board):
    print('  1  2  3')
    for i in range(3):
        for j in range(3):
            if j == 0:
                print(i+1, end='')
            print(f'|{board[i][j]}|', end = '')
        print('\n')

def isFree(x, y, board):
    print(board[x][y])
    if board[x][y] != ' ':
        return False

    return True

def checkWin(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    elif board[2][0] == board[1][1] == board[0][2]:
        return True

    return False
