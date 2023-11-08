class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(row, col, idx, tracking):
            if (row, col) not in tracking:
                tracking[(row, col)] = 1
            else:
                return False
            res = False
            if idx < len(word) and board[col][row] == word[idx]:
                if idx == len(word)-1:
                    return True
                if row > 0 and (row-1, col) not in tracking:
                    _tracking = tracking.copy()
                    res = res or helper(row-1, col, idx+1, _tracking)
                if col > 0 and (row, col-1) not in tracking:
                    _tracking = tracking.copy()
                    res = res or helper(row, col-1, idx+1, _tracking)
                if row < len(board[0])-1 and (row+1, col) not in tracking:
                    _tracking = tracking.copy()
                    res = res or helper(row+1, col, idx+1, _tracking)
                if col < len(board)-1 and (row, col+1) not in tracking:
                    _tracking = tracking.copy()
                    res = res or helper(row, col+1, idx+1, _tracking)
                return res
            else:
                return False
        
        for col in range(len(board)):
            for row in range(len(board[0])):
                if helper(row, col, 0, {}):
                    return True
        
        return False
                