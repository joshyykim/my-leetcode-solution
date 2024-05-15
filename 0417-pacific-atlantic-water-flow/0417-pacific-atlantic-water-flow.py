class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac = set([(0, i) for i in range(len(heights[0]))] + [(i, 0) for i in range(len(heights))])
        atl = set([(len(heights)-1, i) for i in range(len(heights[0]))] + [(i, len(heights[0])-1) for i in range(len(heights))])
        
        queue = list(pac)
        
        def bfs(queue, ocean):
            while queue:
                i, j = queue.pop(0)
                adjacent = ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
                for adj in adjacent:
                    adj_i, adj_j = adj
                    if 0 <= adj_i < len(heights) and 0 <= adj_j < len(heights[0]) and heights[i][j] <= heights[adj_i][adj_j] and adj not in ocean:
                        ocean.add(adj)
                        queue.append(adj)
                        
        bfs(list(pac), pac)
        bfs(list(atl), atl)
        
        for p in pac:
            if p in atl:
                res.append(p)
            
        return res