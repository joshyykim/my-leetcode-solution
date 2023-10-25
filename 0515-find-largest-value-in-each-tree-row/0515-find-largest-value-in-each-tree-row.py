# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def helper(node, depth):
#             if not node: return;
            
#             if len(res) <= depth:
#                 res.append(-pow(2,31)-1)
                
#             if node.val > res[depth]:
#                 res[depth] = node.val
            
#             helper(node.left, depth+1)
#             helper(node.right, depth+1)
            
            
#         helper(root, 0)
#         return res

#         res = []
#         nodes = [root]
#         depth = 0
        
#         while nodes and root:
#             new_nodes = []
#             res.append(float('-inf'))
#             for node in nodes:
#                 if node.left:
#                     new_nodes.append(node.left)
#                 if node.right:
#                     new_nodes.append(node.right)
#                 if res[depth] < node.val:
#                     res[depth] = node.val
#             nodes = new_nodes
#             depth += 1
        
#         return res

        res = []
        nodes = [root]

        while nodes and root:
            res.append(max(node.val for node in nodes))
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
        
        return res