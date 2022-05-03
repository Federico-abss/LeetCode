# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        headPointer = ListNode(0, head)
        cur = headPointer
        temp = head
        sz = 0
        while temp:
            sz += 1
            temp = temp.next
        
        n = sz - n
        while n:
            cur = cur.next
            n -= 1
            
        cur.next = cur.next.next
        return headPointer.next
        