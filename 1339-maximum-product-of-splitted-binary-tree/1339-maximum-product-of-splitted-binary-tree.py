# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def val_to_sum(node, total):
            if not node: return 0
            left_total = val_to_sum(node.left, total)
            right_total = val_to_sum(node.right, total)
            node.val = node.val+left_total+right_total
            return node.val
        
        def max_product(node, total, products):
            if not node: return products
            products = max_product(node.left, total, products)
            products.append((total-node.val) * node.val)
            products = max_product(node.right, total, products)
            return products
        
        modulo = 10 ** 9 + 7
        val_to_sum(root, 0)
        li = max_product(root, root.val, [])
        return pow(max(li),1,modulo)