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
        node = head
        li = []
        li_2 = []
        if node == None or node.next == None:
            return True
        while node.next != None:
            li.append(node.val)
            li_2.insert(0, node.val)
            node = node.next
        # print(li,li_2)
        li.append(node.val)
        li_2.insert(0, node.val)
        print(li,li_2)
        return li == li_2