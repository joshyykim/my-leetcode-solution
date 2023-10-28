# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li = []
        nodes = [root]
        
        while nodes:
            temp = nodes.pop(0)
            if temp:
                nodes.append(temp.left)
                nodes.append(temp.right)
                li.append(temp.val)
        li.sort()
        return li[k-1]