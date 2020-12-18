# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        node = head
        number = 0
        
        while node.next:
            number = number*10 + node.val 
            node = node.next
            
        number = number*10 + node.val + 1
        node = head
            
        for i,d in enumerate(str(number)):
            
            node.val = int(d)
            if not node.next and len(str(number)) > i + 1:
                node.next = ListNode(number%10)
                break
            node = node.next
        
        return head
