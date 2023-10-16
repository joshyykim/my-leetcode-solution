# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        li = []
        res = 0
        
        while head:
            li.append(head.val)
            head = head.next
        
        for i in range(len(li)//2):
            temp_sum = li[i] + li[-(i+1)]
            if res < temp_sum:
                res = temp_sum
        return res