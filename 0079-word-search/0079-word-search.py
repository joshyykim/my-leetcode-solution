class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        count = Counter(sum(board, []))
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        def helper(row, col, idx, tracking):
            if idx == len(word):
                return True
            if row < 0 or row >= len(board[0]) or col < 0 or col >= len(board) or board[col][row] != word[idx] or (row, col) in tracking:
                return False
            
            tracking.add((row, col))
            res = (helper(row-1, col, idx+1, tracking) or
                   helper(row, col-1, idx+1, tracking) or
                   helper(row+1, col, idx+1, tracking) or
                   helper(row, col+1, idx+1, tracking))
            tracking.remove((row, col))
            return res
        
        for col in range(len(board)):
            for row in range(len(board[0])):
                if helper(row, col, 0, set()):
                    return True
        
        return False
                