# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        curr = head
        odd_head = head.next
        odd_curr = odd_head
        while 1:
            if not curr.next.next: break
            if not odd_curr.next.next:
                curr.next = curr.next.next
                curr = curr.next
                break
            curr.next = curr.next.next
            odd_curr.next = odd_curr.next.next
            odd_curr = odd_curr.next
            curr = curr.next
        curr.next = odd_head
        odd_curr.next = None
        return head