# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        cur = head 
        headPtr = ListNode(0, head)
        prevSegments = headPtr
        
        while True:
            explorer = cur
            for _ in range(k):
                if not explorer:
                    return headPtr.next
                
                explorer = explorer.next
                
            prev = None
            segmentTail = cur
            for _ in range(k):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                
            prevSegments.next = prev
            prevSegments = segmentTail
            segmentTail.next = cur
            
        return headPtr.next