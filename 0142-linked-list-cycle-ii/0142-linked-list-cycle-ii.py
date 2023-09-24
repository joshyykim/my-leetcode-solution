# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ### method 1 (using set) => Time: O(n), Space: O(n) ###
        # s = set()
        # curr = head
        # while curr:
        #     if curr in s:
        #         return curr
        #     s.add(curr)
        #     curr = curr.next
        # return None
        
#         ### method 2 (slow & fast, two pointers) ###
#         if not head:
#             return None
#         slow, fast = head, head.next
        
#         while True:
#             if not fast or not fast.next:
#                 return None
            
#             if slow == fast:
                
            
#             slow = slow.next
#             fast = fast.next
        
        curr = head
        while curr:
            if hasattr(curr, "visited"):
                return curr
            else:
                setattr(curr, "visited", 0)
            curr = curr.next
        return None