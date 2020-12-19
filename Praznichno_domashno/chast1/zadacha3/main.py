from tic_tac_toe import *

board = [[' ',' ',' '], [' ',' ',' '],[' ',' ',' ']]

coordinates = [0,0]
for i in range(9):
    drawBoard(board)
    n = i % 2
    print(f"Player{n+1}'s turn:")
    while True:
        coordinates[0] = int(input("Enter x axis coordinate: "))-1
        coordinates[1] = int(input("Enter y axis coordinate: "))-1
        if isFree(coordinates[0], coordinates[1], board):
            break
            
        print("Unvalid coordinates")
        
    if (i % 2) == 0:
        board[coordinates[0]][coordinates[1]] = 'o'
    else:
        board[coordinates[0]][coordinates[1]] = 'x'

    if i >= 4:
        if checkWin(board):
            print(f"Player{n+1} wins")
            break


