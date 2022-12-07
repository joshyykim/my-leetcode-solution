# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(node, res):
            if not node: return res
            res = helper(node.left, res)
            if node.val >= low and node.val <= high:
                res += node.val
            res = helper(node.right, res)
            return res
        return helper(root, 0)