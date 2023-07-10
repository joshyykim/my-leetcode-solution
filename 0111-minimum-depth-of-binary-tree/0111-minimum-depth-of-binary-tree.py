# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = []
        
        def helper(node, d):
            if not node:
                return;
            if not node.left and not node.right:
                depth.append(d)
            helper(node.left, d+1)
            helper(node.right, d+1)
        
        helper(root, 1)
        return min(depth) if depth else 0