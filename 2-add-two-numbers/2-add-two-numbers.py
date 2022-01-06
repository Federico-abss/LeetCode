# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total = self.readList(l1) + self.readList(l2)
        head = ListNode()
        cur = head
        
        while total:
            cur.next = ListNode(total % 10)
            cur = cur.next
            total //= 10
            
        return head.next if head.next else head
        
    
    def readList(self, head: Optional[ListNode]) -> int:
        
        node = head
        result = 0
        power = 0
        while node:
            result += node.val * 10**power
            node = node.next 
            power += 1
            
        return result