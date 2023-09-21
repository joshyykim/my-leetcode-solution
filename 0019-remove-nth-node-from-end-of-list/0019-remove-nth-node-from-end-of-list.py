# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # ### method 1 (iterate twice, store all linked list in the list) Time: O(n), Space: O(n)
        # li = []
        # curr = head
        # while curr:
        #     li.append(curr)
        #     curr = curr.next
        # to_be_removed = li[-n]
        # curr = head
        # while curr:
        #     if curr.next == to_be_removed:
        #         curr.next = to_be_removed.next
        #     if curr == to_be_removed and curr == head:
        #         head = curr.next
        #     curr = curr.next
        # return head
        
        ### method 2 (recursion) 
        def helper(head, curr):
            if not curr:
                return 1
            nth_from_tail = helper(head, curr.next)
            if nth_from_tail == n and curr == head:
                return -1
            elif nth_from_tail == n+1:
                curr.next = curr.next.next
            return nth_from_tail+1
            
        curr = head
        if helper(head, curr) == -1:
            return head.next
        else:
            return head