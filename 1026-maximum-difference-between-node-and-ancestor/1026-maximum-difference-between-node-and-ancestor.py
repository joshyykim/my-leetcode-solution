# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, low, high):
            if not node: return high-low
            if node.val < low:
                res1 = helper(node.left, node.val, high)
                res2 = helper(node.right, node.val, high)
            elif node.val > high:
                res1 = helper(node.left, low, node.val)
                res2 = helper(node.right, low, node.val)
            else:
                res1 = helper(node.left, low, high)
                res2 = helper(node.right, low, high)
            return max(res1, res2)
        return helper(root, root.val, root.val)