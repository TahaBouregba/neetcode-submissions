class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            X = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in X:
                    return False
                X.add(board[row][i])
        for cols in range (9):
            X = set()
            for i in range (9):
                if board[i][cols] == ".":
                    continue
                if board [i][cols] in X:
                    return False
                X.add(board[i][cols])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True


        