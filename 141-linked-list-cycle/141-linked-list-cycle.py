# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        
        hare = head.next.next
        tortoise = head.next
        
        while hare and hare.next and tortoise != hare:
            hare = hare.next.next
            tortoise = tortoise.next
            
        return tortoise == hare