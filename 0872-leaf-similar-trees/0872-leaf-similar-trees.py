# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node, leaf):
            if not node: return leaf
            leaf = helper(node.left, leaf)
            if not node.left and not node.right:
                leaf.append(node.val)
            leaf = helper(node.right, leaf)
            return leaf
        leaf1 = helper(root1, [])
        leaf2 = helper(root2, [])
        return leaf1 == leaf2