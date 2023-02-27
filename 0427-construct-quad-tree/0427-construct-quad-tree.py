"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(grid):
            subSize = len(grid) // 2
            if sum([sum(_) for _ in grid]) / pow(len(grid), 2) == 0:
                return Node(0,1)
            elif sum([sum(_) for _ in grid]) / pow(len(grid), 2) == 1:
                return Node(1,1)
            else:
                return Node(1,0, helper([grid[i][:subSize] for i in range(subSize)]),
                                 helper([grid[i][subSize:] for i in range(subSize)]),
                                 helper([grid[i][:subSize] for i in range(subSize, len(grid))]),
                                 helper([grid[i][subSize:] for i in range(subSize, len(grid))]))
        return helper(grid)