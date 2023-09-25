# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        linked_list_set = set()
        currA, currB = headA, headB
        
        while currA:
            while currB:
                linked_list_set.add(id(currB))
                currB = currB.next
            if id(currA) in linked_list_set:
                return currA
            else:
                currA = currA.next
        return None