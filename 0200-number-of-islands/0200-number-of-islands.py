class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = []
        idx = 0
        
        
        def isFound(i, j):
            for island in islands:
                if (i, j) in island:
                    return True
            return False
        
        def findGround(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or (i, j) in islands[-1]:
                return;
            
            if grid[i][j] == "1":
                islands[-1].add((i,j))
                findGround(i+1, j)
                findGround(i, j+1)
                findGround(i-1, j)
                findGround(i, j-1)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if not isFound(i, j):
                        islands.append(set())
                        findGround(i,j)
                    
        return len(islands)