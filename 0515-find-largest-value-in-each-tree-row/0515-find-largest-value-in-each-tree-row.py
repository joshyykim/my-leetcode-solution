# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(node, depth):
            if not node: return;
            
            if len(res) <= depth:
                res.append(-pow(2,31)-1)
                
            if node.val > res[depth]:
                res[depth] = node.val
            
            helper(node.left, depth+1)
            helper(node.right, depth+1)
            
            
        helper(root, 0)
        return res