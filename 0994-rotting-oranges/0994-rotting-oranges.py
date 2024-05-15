class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rottening(i, j, m):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or (i, j) in found:
                return;
            
            if grid[i][j] == 1:
                return max(findGround(i+1, j, m+1), findGround(i, j+1, m+1), findGround(i-1, j, m+1), findGround(i, j-1, m+1))
            
        queue = []
        cnt, time = 0, -1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue:
            rottens = queue
            queue = []
            for rotten in rottens:
                i, j = rotten
                adjacent = ((i, j-1), (i, j+1), (i-1, j), (i+1, j))
                for adj in adjacent:
                    i, j = adj
                    if  i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == 1:
                        cnt -= 1
                        grid[i][j] = 2
                        queue.append((i, j))
            time += 1
            
        if cnt > 0:
            return -1
        else:
            return max(time, 0)