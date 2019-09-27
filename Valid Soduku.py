def isValidSudoku(board):
    cols = list(zip(*board))
    for i in range(9):
        row = [item for item in board[i] if item != '.']
        col = [item for item in cols[i] if item != '.']
        if len(row) != len(set(row)) or len(col) != len(set(col)):
            return 0

    for i in range(0, 9, 3):
        for k in range(0, 9, 3):
            temp = []
            for j in range(0, 3):
                temp.extend(board[i:i + 3][j][k:k + 3])
            temp = [i for i in temp if i != '.']
            if len(temp) != len(set(temp)):
                print(temp)
                return 0

    return 1


table = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

ans = isValidSudoku(table)
print(ans)
