"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        
        nodeList = [None] * 101
        nodeList[node.val] = Node(node.val)
        stack = [node]
        
        while stack:
            temp = stack.pop(0)
            if not nodeList[temp.val]:
                nodeList[temp.val] = Node(temp.val)
                
            for neighbor in temp.neighbors:
                if not nodeList[neighbor.val]:
                    nodeList[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)
                    
                nodeList[neighbor.val].neighbors.append(nodeList[temp.val])
                
        return nodeList[node.val]