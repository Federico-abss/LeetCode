# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        headPointer = ListNode()
        prev = headPointer
        
        while head and head.next:
            prev.next = head.next
            head.next = prev.next.next
            prev.next.next = head
            prev = head
            head = head.next
            
        return headPointer.next