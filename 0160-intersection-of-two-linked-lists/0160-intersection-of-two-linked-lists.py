# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         linked_list_set = set()
#         currA, currB = headA, headB
        
#         while currA:
#             while currB:
#                 linked_list_set.add(id(currB))
#                 currB = currB.next
#             if id(currA) in linked_list_set:
#                 return currA
#             else:
#                 currA = currA.next
#         return None => O(n*m), O(m)

#         n, m = 0, 0
#         currA, currB = headA, headB
        
#         while currA:
#             n += 1
#             currA = currA.next
        
#         while currB:
#             m += 1
#             currB = currB.next
            
#         move_forward = 0
#         currA, currB = headA, headB
        
#         if n > m:
#             move_forward = n - m
#             for i in range(move_forward):
#                 currA = currA.next
#         elif n < m:
#             move_forward = m - n
#             for i in range(move_forward):
#                 currB = currB.next
        
#         while currA:
#             if currA == currB:
#                 return currA
#             currA, currB = currA.next, currB.next
        
#         return None

        currA, currB = headA, headB
    
        while currA != currB:
            if not currA:
                currA = headB
            else:
                if not currB:
                    currB = headA
                else:
                    currA, currB = currA.next, currB.next
            
        return currA