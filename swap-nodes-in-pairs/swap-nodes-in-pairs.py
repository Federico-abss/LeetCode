# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            
            temp = head.next.next
            head.next.next = head 
            prev.next = head.next
            head.next = temp
            
            prev = head
            head = head.next
        
        return dummy.next
