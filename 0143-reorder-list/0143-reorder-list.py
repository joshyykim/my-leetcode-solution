# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        for i in range((len(stack)+1) // 2):
            curr.val = stack[i]
            curr = curr.next
            if curr:
                curr.val = stack[len(stack)-i-1]
                curr = curr.next