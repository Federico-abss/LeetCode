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
        
        listNodes = dict()
        
        headPointer = Node(0)
        cur = headPointer
        original = head
        while head:
            cur.next = Node(head.val)
            cur = cur.next
            listNodes[head] = cur
            head = head.next
            
        copy = headPointer.next
        while copy:
            if original.random:
                copy.random = listNodes[original.random]
            else:
                copy.random = None
            copy = copy.next
            original = original.next
            
        return headPointer.next
            