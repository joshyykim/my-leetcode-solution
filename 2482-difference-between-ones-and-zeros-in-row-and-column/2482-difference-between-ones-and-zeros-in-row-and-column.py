class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_cnts, col_cnts = [], []
        res = []
        for i in range(len(grid)):
            row_cnts.append(Counter(grid[i]))
        for j in range(len(grid[0])):
            col_cnts.append(Counter([grid[_][j] for _ in range(len(grid))]))
        
        for i in range(len(grid)):
            res.append([])
            for j in range(len(grid[0])):
                res[i].append(row_cnts[i][1] + col_cnts[j][1] - row_cnts[i][0] - col_cnts[j][0])
        return res