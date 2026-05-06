def isValidSudoku(board):
    seen = set()

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
                
            num = board[r][c]

            row_key = (num, "row", r)
            col_key = (num, "col", c)
            box_key = (num, "box", r//3, c//3)

            if row_key in seen or col_key in seen or box_key in seen:
                return False
            
            seen.add(row_key)
            seen.add(col_key)
            seen.add(box_key)

    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","2"],
                     ["6","3",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".",".",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]))