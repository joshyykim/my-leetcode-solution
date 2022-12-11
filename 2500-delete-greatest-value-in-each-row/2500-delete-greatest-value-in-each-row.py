class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        res = 0
        for i in range(m):
            s = []
            for j in range(n):
                tmp = grid[j].pop(grid[j].index(max(grid[j])))
                s.append(tmp)
            res += max(s)
        return res