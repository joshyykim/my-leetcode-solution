# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ### method 1 (iterate twice, store all linked list in the list)
        li = []
        curr = head
        while curr:
            li.append(curr)
            curr = curr.next
        to_be_removed = li[-n]
        curr = head
        while curr:
            if curr.next == to_be_removed:
                curr.next = to_be_removed.next
            if curr == to_be_removed and curr == head:
                head = curr.next
            curr = curr.next
        return head