# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # ### method 1 (Using list) ###
        li = []
        curr = head
        while curr:
            li.append(curr.val)
            curr = curr.next
        # return li[:(len(li)+1)//2] == list(reversed(li[len(li)//2:]))
        return li == list(reversed(li))
        ### method 2 ###