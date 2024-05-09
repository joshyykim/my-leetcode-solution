# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = res = ListNode(0)
        over = 0
        
        while l1 or l2:
            res.next = ListNode(0)
            res = res.next
            if l1 and l2:
                res.val = (l1.val + l2.val + over) % 10
                over = (l1.val + l2.val + over) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                res.val = (l1.val + over) % 10
                over = (l1.val + over) // 10
                l1 = l1.next
            elif l2:
                res.val = (l2.val + over) % 10
                over = (l2.val + over) // 10
                l2 = l2.next
                
        if over != 0:
            res.next = ListNode(over)
            
        return head.next