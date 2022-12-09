# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, min_max):
            if not node: return min_max[1]-min_max[0]
            if node.val < min_max[0]:
                res1 = helper(node.left, [node.val, min_max[1]])
                res2 = helper(node.right, [node.val, min_max[1]])
            elif node.val > min_max[1]:
                res1 = helper(node.left, [min_max[0], node.val])
                res2 = helper(node.right, [min_max[0], node.val])
            else:
                res1 = helper(node.left, min_max)
                res2 = helper(node.right, min_max)
            # print(node.val, min_max, res1, res2)
            if res1 > res2:
                return res1
            else:
                return res2
        return helper(root, [root.val, root.val])