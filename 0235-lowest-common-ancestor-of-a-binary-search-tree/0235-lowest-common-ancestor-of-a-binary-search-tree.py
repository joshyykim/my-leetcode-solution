# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if node.val > p.val and node.val < q.val:
                return node
            elif node == p or node == q:
                return node
            elif node.val < p.val:
                return helper(node.right)
            elif node.val > q.val:
                return helper(node.left)
            
        if p.val > q.val:
            p, q = q, p
        
        return helper(root)