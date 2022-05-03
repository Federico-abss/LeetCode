# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = dict()
        
        sz = 0
        while head:
            sz += 1
            nodes[sz] = head
            head = head.next
        
        if sz == n:
            return nodes.get(2, None)
        
        nodes[sz-n].next = nodes[sz-n+1].next
        return nodes.get(1, None)
        