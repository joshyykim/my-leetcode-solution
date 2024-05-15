class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def findGround(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or (i, j) in found:
                return;
            
            if grid[i][j] == 1:
                found.add((i,j))
                findGround(i+1, j)
                findGround(i, j+1)
                findGround(i-1, j)
                findGround(i, j-1)
            
        found = set()
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i, j) not in found:
                        before = len(found)
                        findGround(i,j)
                        after = len(found)
                        if res < after - before:
                            res = after - before
                    
        return res