# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        allValues = []
        while nodes:
            tmp = nodes.pop()
            allValues.append(tmp.val)
            if tmp.left:
                nodes.append(tmp.left)
            if tmp.right:
                nodes.append(tmp.right)
        allValues.sort()
        res = maxsize
        for i in range(1,len(allValues)):
            diff = allValues[i]-allValues[i-1]
            if diff < res:
                res = diff
        return res