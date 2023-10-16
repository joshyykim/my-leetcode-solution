# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li = []
        left = left-1
        
        while head:
            li.append(head.val)
            head = head.next
        
        reversed_part = list(reversed(li[left:right]))
        new_list = li[:left] + reversed_part + li[right:]
        
        new_node = ListNode()
        new_head = new_node
        
        for i in new_list:
            new_node.next = ListNode(i)
            new_node = new_node.next
            
        return new_head.next