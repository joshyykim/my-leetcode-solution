class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkSubBox, checkVerticalAndHorizontal = False, False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row % 3 == 0 and col % 3 == 0:
                    checkSubBox = True
                
                if checkSubBox:
                    numbers = [_ for _ in range(1,10)]
                    for i in range(row, row+3):
                        for j in range(col, col+3):
                            if board[i][j] != ".":
                                if int(board[i][j]) in numbers:
                                    numbers.remove(int(board[i][j]))
                                else:
                                    return False
                    checkSubBox = False
                    
                if row == col:
                    checkVerticalAndHorizontal = True
                
                if checkVerticalAndHorizontal:
                    numbers = [_ for _ in range(1,10)]
                    for i in range(len(board)):
                        if board[i][col] != ".":
                            if int(board[i][col]) in numbers:
                                numbers.remove(int(board[i][col]))
                            else:
                                return False
                            
                    numbers = [_ for _ in range(1,10)]
                    for j in range(len(board[0])):
                        if board[row][j] != ".":
                            if int(board[row][j]) in numbers:
                                numbers.remove(int(board[row][j]))
                            else:
                                return False
                            
                    checkVerticalAndHorizontal = False
        return True