"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newList = Node(0)
        res = newList
        idxList = []
        curr = head
        
        def getIndex(node, random):
            idx = 0
            while node:
                if node == random:
                    return idx
                node = node.next
                idx += 1
            return idx
        
        while curr:
            newNode = Node(curr.val, curr.next, None)
            idxList.append(getIndex(head, curr.random))
            newList.next = newNode
            newList = newList.next
            curr = curr.next
            
        curr = res.next
        for i in idxList:
            random = res.next
            while i > 0:
                random = random.next
                i -= 1
            curr.random = random
            curr = curr.next
        
        return res.next