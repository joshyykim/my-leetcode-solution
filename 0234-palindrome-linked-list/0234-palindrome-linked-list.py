# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # # ### method 1 (Using list) ###
        # li = []
        # curr = head
        # while curr:
        #     li.append(curr.val)
        #     curr = curr.next
        # return li == list(reversed(li))
    
        ### method 2 ###
        slow, fast = head, head
        stack = []
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast and not fast.next:
            slow = slow.next
            fast = fast.next
            
        while slow:
            if stack.pop(-1) != slow.val:
                return False
            slow = slow.next
        return True
        