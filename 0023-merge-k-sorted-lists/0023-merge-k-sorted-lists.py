# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # method 1 store it into list (n log n)
        merged_list = []
        for li in lists:
            node = li
            while node:
                merged_list.append(node.val)
                node = node.next
        merged_list.sort()
        
        new_node = ListNode()
        new_head = new_node
        
        for val in merged_list:
            new_node.next = ListNode(val)
            new_node = new_node.next
        
        return new_head.next