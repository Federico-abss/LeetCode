# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        even = ListNode()
        curEven = even
        odd = ListNode()
        curOdd = odd
        isOdd = True
        cur = head
        
        while cur:
            if isOdd:
                curOdd.next = cur
                curOdd = curOdd.next
            else:
                curEven.next = cur
                curEven = curEven.next
            isOdd = not isOdd
            cur = cur.next
            
        curEven.next = None
        curOdd.next = even.next
        
        return odd.next
        
        
        