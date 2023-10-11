# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        li.reverse()
        head = ListNode()
        curr = head
        for val in li:
            curr.next = ListNode(val)
            curr = curr.next
        return head.next