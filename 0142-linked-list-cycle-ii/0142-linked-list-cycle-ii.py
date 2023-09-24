class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = set()
        while head:
            if id(head) in li:
                return head
            li.add(id(head))
            head = head.next
        return None